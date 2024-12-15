import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import random
import csv
from datetime import datetime, timedelta

class Participant:
    """
    Класс, представляющий инвестора (участника).
    """
    def __init__(self, pid, join_day, deposit, entry_level):
        self.id = pid
        self.join_day = join_day
        self.deposit = deposit
        self.entry_level = entry_level

        self.daddy = None
        self.grandfather = None
        self.pyramid_level = None

        # Финансовые показатели
        self.earnings = 0.0           # Текущие накопленные проценты
        self.total_earned = 0.0       # Общая сумма заработанных процентов
        self.total_withdrawn = 0.0    # Общая сумма выведенных средств
        self.referral_rewards = 0.0   # Награды за рефералов

        # Баланс и история
        self.CIB = deposit            # Кумулятивный баланс инвестора
        self.children = []            # Прямые рефералы
        self.last_salary_withdraw_day = join_day
        self.working_days_since_withdrawal = 0

    def can_withdraw_salary(self, current_day, is_working_day):
        """
        Проверяет, может ли участник вывести зарплату.
        """
        if not is_working_day:
            return False

        if self.earnings <= 0:
            return False

        if self.working_days_since_withdrawal < 2:
            return False

        return True

    def add_earnings(self, amount):
        """
        Добавляет заработок участнику.
        """
        self.earnings += amount
        self.total_earned += amount
        self.CIB += amount

    def withdraw_earnings(self, fee_percent, company_commission_percent):
        """
        Обрабатывает вывод заработка с учетом комиссий.
        Возвращает словарь с распределением сумм.
        """
        if self.earnings <= 0:
            return None

        withdrawal = self.earnings
        self.earnings = 0

        # Расчет комиссий и выплат
        withdrawal_fee = withdrawal * fee_percent
        net_amount = withdrawal - withdrawal_fee

        company_commission = net_amount * company_commission_percent

        daddy_commission = net_amount * 0.10 if self.daddy else 0
        grandfather_commission = net_amount * 0.05 if self.grandfather else 0

        participant_amount = (net_amount - company_commission -
                              daddy_commission - grandfather_commission)

        # Обновляем балансы
        self.CIB -= (withdrawal - participant_amount)
        self.total_withdrawn += participant_amount

        return {
            'withdrawal': withdrawal,
            'withdrawal_fee': withdrawal_fee,
            'company_commission': company_commission,
            'daddy_commission': daddy_commission,
            'grandfather_commission': grandfather_commission,
            'participant_amount': participant_amount
        }


class PyramidScheme:
    """
    Класс для моделирования пирамидальной схемы с улучшенным отслеживанием финансов.
    """
    def __init__(self, days=30, fee_percent=5.0, daily_interest_rate=3.3, option=1,
                 referral_reward=0.0, deposit_reward_percent=0.0,
                 dynamic_coefficient_function=None,
                 levels=None,
                 weights_levels=None,
                 num_referrals_list=None,
                 weights_referrals=None):

        # Базовые параметры
        self.days = days
        self.fee_percent = fee_percent / 100.0
        self.daily_interest_rate = daily_interest_rate / 100.0
        self.company_commission_percent = 0.05  # 5% комиссия компании

        # Параметры реферальной системы
        self.option = option
        self.referral_reward = referral_reward
        self.deposit_reward_percent = deposit_reward_percent / 100.0

        # Функция динамического коэффициента
        self.dynamic_coefficient_function = dynamic_coefficient_function

        # Инициализация уровней депозитов
        self.levels = levels or {
            1: 200, 2: 400, 3: 800, 4: 1300, 5: 2500,
            6: 3700, 7: 5000, 8: 8000, 9: 12000, 10: 23000
        }

        # Веса уровней депозитов
        self.weights_levels = weights_levels or {
            1: 10000, 2: 8000, 3: 6000, 4: 1000, 5: 700,
            6: 200, 7: 100, 8: 10, 9: 2, 10: 1
        }
        self.weights_levels_norm = self._normalize_weights(self.weights_levels)

        # Инициализация параметров рефералов
        self.num_referrals_list = num_referrals_list or list(range(13))
        self.weights_referrals = weights_referrals or {
            i: w for i, w in zip(
                range(10),
                [10000, 8000, 6000, 1000, 700, 200, 100, 10, 2, 1]
            )
        }
        self.weights_referrals_norm = self._normalize_weights(self.weights_referrals)

        # Хранилища данных
        self.participants = []
        self.current_id = 0

        # Инициализация ежедневной статистики
        self.daily_stats = {day: {
            'CIP': 0.0,                    # Кумулятивный баланс платформы
            'total_CIB': 0.0,              # Сумма балансов инвесторов
            'active_investors': 0,         # Количество активных инвесторов
            'new_deposits': 0.0,           # Новые депозиты
            'total_deposits': 0.0,         # Общая сумма депозитов
            'daily_interest_paid': 0.0,    # Выплаченные проценты
            'withdrawals': 0.0,            # Выводы средств
            'fees_collected': 0.0,         # Собранные комиссии
            'company_profit': 0.0,         # Прибыль компании
            'referral_rewards': 0.0,       # Реферальные награды
            'avg_referrals': 0.0,          # Среднее количество рефералов
            'avg_entry_level': 0.0         # Средний уровень входа
        } for day in range(1, days + 1)}

    def _normalize_weights(self, weights_dict):
        """
        Нормализует веса для получения вероятностей.
        """
        values = np.array(list(weights_dict.values()), dtype=float)
        return values / np.sum(values)

    def _is_working_day(self, day):
        """
        Определяет, является ли день рабочим.
        """
        return (day % 7) not in [6, 0]  # Пн-Пт: True; Сб-Вс: False

    def _process_daily_interest(self, day):
        """
        Обрабатывает начисление ежедневных процентов (compound interest).
        """
        if not self._is_working_day(day):
            return 0.0

        total_interest = 0.0
        for p in self.participants:
            if p.join_day <= day:
                # Compound interest: use p.CIB
                interest = p.CIB * self.daily_interest_rate
                p.add_earnings(interest)
                total_interest += interest

                # Increment working days since last withdrawal
                p.working_days_since_withdrawal += 1

        return total_interest

    def _process_withdrawals(self, day):
        """
        Обрабатывает выводы средств участников.
        """
        total_withdrawals = 0.0
        total_fees = 0.0
        company_profit = 0.0

        for p in self.participants:
            if p.can_withdraw_salary(day, self._is_working_day(day)):
                withdrawal_info = p.withdraw_earnings(
                    self.fee_percent,
                    self.company_commission_percent
                )
                if withdrawal_info:
                    total_withdrawals += withdrawal_info['withdrawal']
                    total_fees += withdrawal_info['withdrawal_fee']
                    company_profit += withdrawal_info['company_commission']

                    # Комиссии рефералам
                    if p.daddy:
                        p.daddy.add_earnings(withdrawal_info['daddy_commission'])
                    if p.grandfather:
                        p.grandfather.add_earnings(withdrawal_info['grandfather_commission'])

                    p.working_days_since_withdrawal = 0

        return total_withdrawals, total_fees, company_profit

    def _create_new_investor(self, day):
        """
        Создает нового инвестора с выбранными параметрами.
        """
        # Only increment once
        self.current_id += 1

        # Выбираем уровень входа на основе весов
        entry_level = np.random.choice(
            list(self.weights_levels.keys()),
            p=self.weights_levels_norm
        )
        deposit = self.levels[entry_level]

        investor = Participant(
            self.current_id,
            day,
            deposit,
            entry_level
        )
        return investor

    def _assign_referrers(self, new_investors):
        """
        Назначает рефереров новым инвесторам на основе весовой вероятности.
        """
        for investor in new_investors:
            # Determine how many referrals this investor should have based on weights
            num_referrals = np.random.choice(
                self.num_referrals_list,
                p=self.weights_referrals_norm
            )

            potential_referrals = [p for p in self.participants if p != investor]

            if potential_referrals and num_referrals > 0:
                # Limit num_referrals to available potential referrals
                num_referrals = min(num_referrals, len(potential_referrals))
                selected_referrals = random.sample(potential_referrals, num_referrals)

                # First selected referral becomes the 'daddy'
                investor.daddy = selected_referrals[0]
                investor.daddy.children.append(investor)

                # If there's a daddy's daddy, that becomes the grandfather
                if investor.daddy.daddy:
                    investor.grandfather = investor.daddy.daddy

                # Update pyramid level
                if investor.daddy.pyramid_level is not None:
                    investor.pyramid_level = investor.daddy.pyramid_level + 1
                else:
                    investor.pyramid_level = 1

                # Apply referral rewards if option 2 is selected
                if self.option == 2:
                    # Only give rewards for the first 12 referrals
                    if len(investor.daddy.children) <= 12:
                        reward = (
                            self.referral_reward if self.referral_reward > 0
                            else investor.deposit * self.deposit_reward_percent
                        )
                        investor.daddy.referral_rewards += reward
                        investor.daddy.CIB += reward
            else:
                # If no referrers available or num_referrals is 0, this is a root node
                investor.pyramid_level = 1

    def run_simulation(self):
        """
        Запускает симуляцию пирамидальной схемы.
        """
        CIP = 0.0  # Кумулятивный баланс платформы

        for day in range(1, self.days + 1):
            # Определяем количество новых инвесторов
            new_investors_count = 1
            if self.dynamic_coefficient_function:
                new_investors_count = max(
                    1,
                    int(round(self.dynamic_coefficient_function(day)))
                )

            # Создаем новых инвесторов
            new_investors = []
            daily_new_deposits = 0.0

            for _ in range(new_investors_count):
                investor = self._create_new_investor(day)
                new_investors.append(investor)
                self.participants.append(investor)
                daily_new_deposits += investor.deposit
                CIP += investor.deposit

            # Назначаем рефереров
            self._assign_referrers(new_investors)

            # Начисляем проценты
            daily_interest = self._process_daily_interest(day)
            CIP -= daily_interest

            # Обрабатываем выводы
            withdrawals, fees, company_profit = self._process_withdrawals(day)
            CIP -= withdrawals
            CIP += fees           # Комиссии возвращаются в CIP
            CIP += company_profit # Прибыль компании тоже увеличивает CIP

            # Обновляем статистику
            self._update_daily_stats(
                day, CIP, daily_new_deposits,
                daily_interest, withdrawals,
                fees, company_profit
            )

    def _update_daily_stats(self, day, CIP, new_deposits, interest_paid,
                           withdrawals, fees, company_profit):
        """
        Обновляет ежедневную статистику.
        """
        stats = self.daily_stats[day]
        active_investors = len([p for p in self.participants if p.join_day <= day])

        stats['CIP'] = CIP
        stats['total_CIB'] = sum(p.CIB for p in self.participants)
        stats['active_investors'] = active_investors
        stats['new_deposits'] = new_deposits
        stats['total_deposits'] = sum(p.deposit for p in self.participants)
        stats['daily_interest_paid'] = interest_paid
        stats['withdrawals'] = withdrawals
        stats['fees_collected'] = fees
        stats['company_profit'] = company_profit

        if active_investors > 0:
            active_participants = [p for p in self.participants if p.join_day <= day]
            stats['avg_referrals'] = sum(len(p.children) for p in active_participants) / active_investors
            stats['avg_entry_level'] = sum(p.entry_level for p in active_participants) / active_investors

    def save_csv(self, filename='platform_daily_report.csv'):
        """
        Сохраняет ежедневную статистику в CSV файл.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = [
                'День',
                'CIP ($)',
                'Сумма CIB ($)',
                'Разница CIP-CIB ($)',
                'Активных инвесторов',
                'Новые депозиты ($)',
                'Общая сумма депозитов ($)',
                'Выплаченные проценты ($)',
                'Выводы средств ($)',
                'Комиссии ($)',
                'Прибыль компании ($)',
                'Средний уровень входа',
                'Среднее кол-во рефералов'
            ]

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for day in range(1, self.days + 1):
                stats = self.daily_stats[day]
                writer.writerow({
                    'День': day,
                    'CIP ($)': round(stats['CIP'], 2),
                    'Сумма CIB ($)': round(stats['total_CIB'], 2),
                    'Разница CIP-CIB ($)': round(stats['CIP'] - stats['total_CIB'], 2),
                    'Активных инвесторов': stats['active_investors'],
                    'Новые депозиты ($)': round(stats['new_deposits'], 2),
                    'Общая сумма депозитов ($)': round(stats['total_deposits'], 2),
                    'Выплаченные проценты ($)': round(stats['daily_interest_paid'], 2),
                    'Выводы средств ($)': round(stats['withdrawals'], 2),
                    'Комиссии ($)': round(stats['fees_collected'], 2),
                    'Прибыль компании ($)': round(stats['company_profit'], 2),
                    'Средний уровень входа': round(stats['avg_entry_level'], 2),
                    'Среднее кол-во рефералов': round(stats['avg_referrals'], 2)
                })

    # --- NEW PLOTLY METHODS BELOW ---

    def plot_cumulative_balance(self):
        """
        Строит интерактивный график кумулятивного баланса платформы (CIP) и суммы CIB с помощью Plotly.
        """
        days = list(range(1, self.days + 1))
        cip_values = [self.daily_stats[d]['CIP'] for d in days]
        cib_values = [self.daily_stats[d]['total_CIB'] for d in days]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=days, y=cip_values, mode='lines+markers',
                                 name='CIP', line=dict(color='blue', width=2)))
        fig.add_trace(go.Scatter(x=days, y=cib_values, mode='lines+markers',
                                 name='Сумма CIB', line=dict(color='red', width=2, dash='dash')))

        fig.update_layout(
            title='Динамика CIP и суммы CIB по дням',
            xaxis_title='День',
            yaxis_title='Баланс ($)',
            legend=dict(x=0.05, y=0.95),
            hovermode='x unified'
        )
        fig.show()

    def plot_financial_metrics(self):
        """
        Строит интерактивный график основных финансовых показателей (новые депозиты, проценты, выводы, комиссии) по дням.
        """
        days = list(range(1, self.days + 1))
        new_deposits = [self.daily_stats[d]['new_deposits'] for d in days]
        daily_interest_paid = [self.daily_stats[d]['daily_interest_paid'] for d in days]
        withdrawals = [self.daily_stats[d]['withdrawals'] for d in days]
        fees_collected = [self.daily_stats[d]['fees_collected'] for d in days]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=days, y=new_deposits, mode='lines+markers',
                                 name='Новые депозиты', line=dict(width=2)))
        fig.add_trace(go.Scatter(x=days, y=daily_interest_paid, mode='lines+markers',
                                 name='Выплаченные проценты', line=dict(width=2)))
        fig.add_trace(go.Scatter(x=days, y=withdrawals, mode='lines+markers',
                                 name='Выводы средств', line=dict(width=2)))
        fig.add_trace(go.Scatter(x=days, y=fees_collected, mode='lines+markers',
                                 name='Комиссии', line=dict(width=2)))

        fig.update_layout(
            title='Ежедневные финансовые показатели',
            xaxis_title='День',
            yaxis_title='Сумма ($)',
            legend=dict(x=0.05, y=0.95),
            hovermode='x unified'
        )
        fig.show()

    def plot_investor_metrics(self):
        """
        Строит интерактивный график показателей инвесторов.
        """
        days = list(range(1, self.days + 1))
        active_investors = [self.daily_stats[d]['active_investors'] for d in days]
        avg_entry_level = [self.daily_stats[d]['avg_entry_level'] for d in days]
        avg_referrals = [self.daily_stats[d]['avg_referrals'] for d in days]

        # Plot active investors
        fig1 = px.line(
            x=days,
            y=active_investors,
            title='Количество активных инвесторов',
            labels={'x': 'День', 'y': 'Количество активных инвесторов'}
        )
        fig1.show()

        # Plot average entry level and average referrals on the same figure
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=days, y=avg_entry_level, mode='lines+markers',
            name='Средний уровень входа',
            line=dict(color='blue', width=2)
        ))
        fig2.add_trace(go.Scatter(
            x=days, y=avg_referrals, mode='lines+markers',
            name='Среднее кол-во рефералов',
            line=dict(color='red', width=2)
        ))
        fig2.update_layout(
            title='Средние показатели инвесторов',
            xaxis_title='День',
            yaxis_title='Значение',
            legend=dict(x=0.05, y=0.95),
            hovermode='x unified'
        )
        fig2.show()

    def plot_new_deposits_vs_days(self):
        """
        Новые депозиты ($) / Дни
        """
        days = list(range(1, self.days + 1))
        new_deposits = [self.daily_stats[d]['new_deposits'] for d in days]

        fig = px.line(
            x=days,
            y=new_deposits,
            labels={'x': 'День', 'y': 'Новые депозиты ($)'},
            title='Новые депозиты ($) vs. Дни'
        )
        fig.show()

    def plot_total_deposits_vs_days(self):
        """
        Общая сумма депозитов ($) / Дни
        """
        days = list(range(1, self.days + 1))
        total_deposits = [self.daily_stats[d]['total_deposits'] for d in days]

        fig = px.line(
            x=days,
            y=total_deposits,
            labels={'x': 'День', 'y': 'Общая сумма депозитов ($)'},
            title='Общая сумма депозитов ($) vs. Дни'
        )
        fig.show()

    def plot_new_deposits_vs_withdrawals(self):
        """
        Новые депозиты ($) vs. Выводы средств ($) (Scatter plot for comparison)
        """
        # We'll make a scatter plot with new deposits on x-axis and withdrawals on y-axis
        days = list(range(1, self.days + 1))
        new_deposits = [self.daily_stats[d]['new_deposits'] for d in days]
        withdrawals = [self.daily_stats[d]['withdrawals'] for d in days]

        fig = px.scatter(
            x=new_deposits,
            y=withdrawals,
            labels={'x': 'Новые депозиты ($)', 'y': 'Выводы средств ($)'},
            title='Новые депозиты ($) vs. Выводы средств ($)'
        )
        fig.update_traces(mode='markers+text', marker=dict(size=8, color='blue', symbol='circle'))
        fig.show()


def run_pyramid_simulation():
    """
    Функция для запуска симуляции с пользовательскими параметрами (используем значения по умолчанию).
    """
    print("\n=== Конфигурация симуляции пирамидальной схемы ===")

    # Using default values instead of input
    days = 210
    fee_percent = 20.0
    daily_interest = 2.0
    option = 2
    referral_reward = 0.0
    deposit_reward_percent = 15.0

    # Функция динамического коэффициента (пример)
    def dynamic_coefficient(day):
        midpoint = days / 2
        max_investors = 10
        a = max_investors / (midpoint ** 2)
        return max(0.1, -a * (day - midpoint) ** 2 + max_investors)

    # Создание и запуск симуляции
    print("\nЗапуск симуляции...")
    scheme = PyramidScheme(
        days=days,
        fee_percent=fee_percent,
        daily_interest_rate=daily_interest,
        option=option,
        referral_reward=referral_reward,
        deposit_reward_percent=deposit_reward_percent,
        dynamic_coefficient_function=dynamic_coefficient
    )

    scheme.run_simulation()

    # Сохранение и визуализация результатов
    scheme.save_csv('platform_daily_report.csv')
    print("\nРезультаты сохранены в platform_daily_report.csv")

    print("\nПостроение интерактивных графиков в Plotly...")

    # Прежние графики
    scheme.plot_cumulative_balance()
    scheme.plot_financial_metrics()
    scheme.plot_investor_metrics()

    # Новые графики
    scheme.plot_new_deposits_vs_days()
    scheme.plot_total_deposits_vs_days()
    scheme.plot_new_deposits_vs_withdrawals()


if __name__ == "__main__":
    run_pyramid_simulation()
