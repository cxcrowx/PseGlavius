**English Translation:**

**General Recommendations on Style and Interface**  
**Color Scheme:** Use a neutral light background (shades of white or light gray), contrasting accent colors for buttons (e.g., rich blue or purple), and calm pastel tones for block backgrounds.

**Fonts:** A legible sans-serif font (e.g., Inter, Roboto, or Open Sans).  
Font sizes:  
- Headlines: 24-32px  
- Subheadings: 18-20px  
- Main text: 14-16px

**Icons and Images:** Use simple, clear icons, preferably in vector format. Place them near corresponding headings or functions.

**Buttons:** Make them large with rounded corners. Button color: accent color; text: bold white. For example: button background #5569FF, text #FFFFFF.

**Spacing and Grid:** Use a convenient grid (12 columns), maintain margins and spacing for an airy layout. Leave about 20-40px of vertical space between blocks.

**User Friendly:** Minimize unnecessary text, use brief, clear headings, tooltips on hover, and a clear visual hierarchy.

**Project Structure**  
A file structure with development priority and easy navigation: start with access forms (login, registration), then the main hub, then the profile and extended features.

```
project/
│
├─ index.html               // Welcome page
├─ login.html               // Login
├─ register.html            // Registration
├─ recover-password.html    // Password Recovery
│
├─ main.html                // Main hub
├─ user-dashboard.html      // User’s personal dashboard
├─ marketplace.html         // Marketplace for upgrades
├─ ranking-system.html      // Ranks
├─ account-levels.html      // Account levels, leaderboard
├─ payouts.html             // Payout structure
├─ partner-program.html     // Partner program
├─ additional-features.html // Additional features: insurance, geography, NFT
├─ investor-example.html    // Investor example
├─ income-sources.html      // Income sources
├─ conclusion.html          // Conclusion
│
├─ about-us.html            // About the company
├─ faq.html                 // FAQ
├─ contact-support.html     // Support
├─ roadmap.html             // Roadmap
├─ profit-calculator.html   // Profitability calculator
├─ international.html       // International expansion
│
├─ purchase-equipment.html  // New layout for purchasing drones and upgrades
├─ transactions.html        // Transaction history, balance management
│
├─ css/
│  ├─ style.css
│  └─ responsive.css
│
├─ js/
│  ├─ main.js
│  └─ slider.js
│
└─ images/
   ├─ ... (icons, logos, charts)
```

**Detailed Description of Slides and Elements**

**index.html (1 slide)**  
**Slide 1: Welcome Page**  
- Heading (large, centered): "Welcome to Pseglavius Drones Ltd."  
  Style: bold, 32px, dark gray (#333)  
- Subheading: "Investing in autonomous drone fleets — the future of logistics"  
  Style: 18px, normal, #555  
- Buttons:  
  "Login" (goes to login.html)  
  "Register" (goes to register.html)  
  Button style: background #5569FF, white text, semi-bold font, 16px.  
- Logo icon (logo.png) in the top-left corner, size ~50px.  
- Layout: Logo in top-left, heading and subheading centered on the slide, buttons below heading.

**login.html (1 slide)**  
**Slide 1: Login**  
- Heading: "Login to Your Account" (centered, 24px, #333)  
- Input fields: Email/Username, Password. Labels above fields in small 14px font.  
- "Login" button below the fields, about 200px wide, centered.  
- "Forgot your password?" link in small font (14px), below the button in blue.  
- Form style: fields with soft shadows and rounded corners.

**register.html (2 slides)**  
**Slide 1: Registration Data**  
- Heading: "Create an Account" (24px, #333, centered)  
- Fields: Email, Username, Password, Repeat Password. Short labels (14px).  
- "Register" button below the fields.  
- Below the button a link: "Already have an account? Login" (links to login.html).

**Slide 2: Terms**  
- Terms text (14px, #555) in a scrollable box.  
- Checkbox: "I agree to the terms" at the bottom.  
- "Confirm" button activates after checking the box.

**recover-password.html (1 slide)**  
**Slide 1: Password Recovery**  
- Heading: "Password Recovery" (24px, #333)  
- Email input field  
- "Send Instructions" button  
- "Return to Login" link below the button.

**main.html (3 slides)**  
**Slide 1: Main Hub**  
- Logo in top-left corner, menu at the top (icons to navigate to dashboard, marketplace, etc.).  
- Large heading: "Main Panel" (24px, #333)  
- Icon-cards: Marketplace, Ranking, Partner Program, Additional Features. Each icon (~64px), with a short 1-2 sentence description beneath. Arrange in a 2x2 grid.  
- News banner (banner-improvements.png) at the bottom of the slide.

**Slide 2: Equipment and Upgrades**  
- Heading "Your Upgrades" (20px, #333), below it a horizontal slider with upgrade icons (battery-upgrade.png, propellers.png).  
- A short text under each icon (14px, #555) describing the upgrade.  
- "Go to Marketplace" button at the end of the slide.

**Slide 3: NFT and Geolocation**  
- NFT icon (nft-icon.png) on the left, text (14-16px) on the right about the benefits of owning NFTs.  
- Below it a map (map.png) and text about choosing areas to optimize income.  
- Buttons: "More About Features" (leads to additional-features.html), "View Investor Example" (leads to investor-example.html).

**user-dashboard.html (2 slides)**  
**Slide 1: User Status**  
- Heading: "Hello, [Name]" (24px, #333)  
- Status cards: Number of drones, Account level, Current rank, Daily income. Each card with an icon (dashboard-icon.png), large number (20px), and a 14px label.  
- Light infographic: a small circular income chart.

**Slide 2: Statistics and Activity**  
- Charts or line graphs (with small labels on axes).  
- Buttons "Upgrade Drones", "View Payouts" — links to marketplace.html and payouts.html.

**marketplace.html (2 slides)**  
**Slide 1: Upgrade Store**  
- Battery, propeller icons in a grid, each with a price tag and brief description.  
- "Buy" button below each upgrade.  
- Filters (list, grid, sort by price).

**Slide 2: Shopping Cart**  
- List of selected upgrades, "+" "-" buttons to adjust quantities.  
- "Checkout" button.

**ranking-system.html (1 slide)**  
**Slide 1: Ranks**  
- Ranks table: Basic, Silver, Gold, Platinum.  
- Brief description: "The more flight hours, the lower the commission."  
- Progress indicator towards the next rank (progress bar).

**account-levels.html (2 slides)**  
**Slide 1: Account Levels**  
- A levels scale with rewards and prize icons.  
- Short text: "Invite partners to level up and earn bonuses."

**Slide 2: Leaderboard**  
- Top accounts table (name, level, number of invites).  
- "Star" icon for top positions.

**payouts.html (2 slides)**  
**Slide 1: Payout Structure**  
- Table with levels, rates, coefficients.  
- Short text about the influence of ranks and upgrades.

**Slide 2: Dynamic Calculator**  
- Link to profit-calculator.html  
- Example of final income changes with different parameters.

**partner-program.html (2 slides)**  
**Slide 1: Partners and Referrals**  
- Referral level scheme (icons, arrows).  
- Percentage table for each level.

**Slide 2: Bonus Utilization**  
- Description: "Use bonuses for upgrades or withdrawals."  
- Buttons "Marketplace" and "Withdraw Funds."

**additional-features.html (3 slides)**  
**Slide 1: Maintenance and Insurance**  
- Drone icons, plan prices.  
- Short text on insurance benefits.

**Slide 2: Geography**  
- Map highlighting city center and suburbs.  
- Text: "+50% to income in the center."

**Slide 3: NFT**  
- NFT icon, text about liquidity and resale.

**investor-example.html (1 slide)**  
**Slide 1: Investor Example**  
- Short narrative: "At level 7 with upgrades you earn more than X USDT/year."  
- A graphical comparison of income without and with upgrades.

**income-sources.html (3 slides)**  
**Slide 1: General Overview**  
- Icons: rental, delivery, advertising.  
- Brief explanations.

**Slide 2: Rental and Commission**  
- Text with income formula.  
- Simple graph of income dependency on number of orders.

**Slide 3: Advertising**  
- Image of a drone with a screen.  
- Text on higher rates in busy areas.

**conclusion.html (1 slide)**  
**Slide 1: Conclusion**  
- Short summary of opportunities.  
- "Start Investing" button.

**about-us.html (1 slide)**  
**Slide 1: About the Company**  
- Team banner (about-team.png).  
- Text about mission and values.  
- "Contact" button -> contact-support.html

**faq.html (1 slide)**  
**Slide 1: FAQ**  
- Accordion with questions and answers (faq-icon.png to the left of the heading).  
- Concise answer texts.

**contact-support.html (1 slide)**  
**Slide 1: Support**  
- Form: Name, Email, Message  
- "Send" button  
- Support contacts at the bottom (email, chat).

**roadmap.html (1 slide)**  
**Slide 1: Roadmap**  
- A linear scale with future releases (roadmap-icon.png).  
- Brief description of key stages.

**profit-calculator.html (1-2 slides)**  
**Slide 1: Profit Calculator**  
- Input fields: number of drones, selected level, upgrades (checkboxes).  
- "Calculate" button.  
- Display the result in large font.  
- (Optional Slide 2): Detailed calculation.

**international.html (1 slide)**  
**Slide 1: International Expansion**  
- World map with highlighted regions (international-icon.png).  
- Short text about expansion benefits.  
- "Learn More" button.

**Conclusion**  
The presented architecture and detailed description of slides greatly simplify the development process. We started with basic authorization pages, then moved to the main hub and further into internal pages. Each page is structured simply and clearly, using icons, buttons, banners, and text with stylish and practical recommendations. This approach ensures user-friendliness and makes it easier for developers to implement functionality step-by-step, gradually expanding the project’s capabilities.

Below is an additional layout for managing purchases, payments, and transactions. This layout focuses on the procedure for purchasing new equipment (drones) and upgrades, as well as choosing the payment network (TRC20, Polygon, etc.). It provides a convenient step-by-step interface that makes the transaction process as understandable as possible for the user.

We also add a supplementary layout for viewing the transaction history and managing the balance. This allows the user to track their operations, top up the balance, withdraw funds, and view order status.

**purchase-equipment.html (4-5 slides)**  
**Main Idea**  
The page is divided into logical steps of the purchase process. The user first chooses drones and upgrades, then selects the payment network, confirms the transaction, and makes the payment. All with a user-friendly interface.

**General Style Recommendations**  
- Process Steps: At the top of the page, place a progress bar with stages: "Select Equipment" → "Upgrades" → "Select Network and Payment Method" → "Confirmation" → "Payment".  
- Fonts and Colors: Use the already set project style. Headlines ~24px, text 14-16px, buttons in the accent color (#5569FF), small labels for fields.  
- Icons: Use drone, upgrade icons, and logos of networks (like TRC20/Polygon) for clarity.

**Slide 1: Selecting Equipment (Drones)**  
Contents:
- Heading: "Select Drones to Purchase" (24px, #333, centered).  
- Grid of drone cards: Each card has a drone icon (drone.png), short specs (flight hours, speed, base earnings).  
- Under the icon: "Drone Model X" (18px, bold), short text: "High speed, up to 20 hrs flight" (14px, #555).  
- Price in USDT (large, 16px), "Add to Cart" button.  
- A sidebar or bottom block "Cart": displays selected drones with the option to remove or change quantity.  
- "Next" button at the bottom of the slide, centered, bright (#5569FF, white text "Continue") leads to the next slide.

**Slide 2: Adding Upgrades**  
Contents:
- Heading: "Select Upgrades for Your Drones"  
- Grid of upgrades: Battery (battery-upgrade.png), propellers (propellers.png), spare parts. Each with a short description: "Battery +20% flight time", "Propellers +10% speed", "Spare parts reduce downtime."  
- Under each upgrade: price in USDT, "Add to Selected Drones" button.  
- A side or bottom panel with order summary: shows already selected drones and upgrades, total amount.  
- Buttons:  
  "Back" to return to the previous slide  
  "Next" to go to the network selection

**Slide 3: Selecting Network and Payment Method**  
Contents:
- Heading: "Choose Payment Network"  
- Short text: "You can pay in USDT via TRC20 or Polygon. Select a convenient network."  
- Network cards:
  - TRC20 card with logo, short description ("Low fees, fast transaction"). "Choose TRC20" button.
  - Polygon card with logo, description ("Scalable, low fees"). "Choose Polygon" button.
- After choosing a network: a field or displayed address to send funds.  
- Side panel with order summary: chosen drones and upgrades, final USDT amount.  
- Buttons: "Back" and "Next"  
- Additional info: transaction speed, security, and a link to payment FAQ.

**Slide 4: Order Confirmation**  
Contents:
- Heading: "Order Confirmation"  
- A table or confirmation block:
  - List of drones, their quantities, and costs
  - List of upgrades with prices
  - Total amount in USDT
- "Confirm and Proceed to Payment" button  
- "Back" button for adjustments  
- Style: A neat, clear table. Highlight total sum in bold, large font.

**Slide 5: Payment**  
Contents:
- Heading: "Order Payment"  
- Depending on the chosen network, display an address to send funds (for example, a field with the address, "Copy Address" button).
- A QR code for quick payment (if applicable)  
- Instructions: "Transfer X USDT to the given address. After the network confirms, your order will be fulfilled."  
- Transaction status indicator (e.g., a progress bar or waiting animation).  
- Button "Go to Transaction History" or "Return to Main" if payment is complete.

**transactions.html (2-3 slides)**  
Purpose: View transaction history, top up balance, withdraw funds.

**Slide 1: Transaction History**  
- Heading: "Transaction History" (24px, #333)  
- Table: Date, Operation Type (Drone/Upgrade Purchase), Amount, Status (success, pending).  
- Search or date filter.  
- CSV download icon, "Refresh" button to update list.  
- "Go to Top-up Balance" button.

**Slide 2: Balance Top-up**  
- Heading: "Top up Balance"  
- Network selection (as on the purchase page), generated deposit address.  
- Instructions for depositing funds.  
- After sending funds, the user can refresh the transaction history to see the top-up.

**(Optional Slide 3): Withdraw Funds**  
- Heading: "Withdraw Funds"  
- Field to enter withdrawal amount, select network.  
- "Submit Withdrawal Request" button.  
- Short description of withdrawal fees.

**Conclusion**  
Added layout purchase-equipment.html for the full purchase cycle of drones and upgrades, including network choice (TRC20/Polygon) and step-by-step payment instructions.  
Added layout transactions.html for balance management, viewing transaction history, and handling top-ups and withdrawals.  
All in a unified style, with clear icons, concise headings, neat tables, and helpful tooltips. The transaction process is broken down into logical steps, improving user convenience and reducing errors.  
The user interface is focused on simplicity: from product selection to payment confirmation. Each stage includes clear instructions and visual aids (icons, QR codes, copy address buttons). This approach extends the project’s capabilities and enhances the user experience (UX).

---

**Classification-Categorization:**  
- **Domain:** Web Design / UI/UX and Front-End Development  
- **Category:**  
  - UI/UX Design Guidelines  
  - Website Architecture and Navigation Structure  
  - Style Guide and Branding (Colors, Fonts, Icons)  
  - Page Layouts and Content Strategy  
  - Interaction Design (Buttons, Forms, Tooltips)  
  - Payment and Transaction Flows (E-commerce Integration)  
  - User Onboarding (Registration, Login)  
  - Internationalization and Scaling Features

---

**TODO Step-by-Step List for the Next Text:**  
1. **Refine Visual Hierarchy:**  
   - Emphasize the most important elements on each page (headings, CTAs)  
   - Ensure consistent sizing and spacing throughout.

2. **Add Detailed Interaction Patterns:**  
   - Specify hover states, focus states for input fields and buttons.  
   - Include animations or transitions where appropriate.

3. **Expand Accessibility Guidelines:**  
   - Provide recommendations for color contrast compliance.  
   - Include instructions for alt-text on images and icons.  
   - Suggest proper ARIA roles for interactive elements.

4. **Incorporate Responsive Design Details:**  
   - Break down how each layout adapts to different screen sizes (desktop, tablet, mobile).  
   - Provide mobile-first design considerations.

5. **Include User Flows and Wireframes:**  
   - Add step-by-step user journey maps or flowcharts.  
   - Provide rough sketches or wireframes to visually represent page layouts.

6. **Detail Content Management:**  
   - Indicate how texts, images, and icons might be dynamically loaded or updated.  
   - Suggest a naming convention and storage strategy for new assets.

7. **Outline Testing and Iteration Plans:**  
   - Propose usability testing scenarios.  
   - Define a feedback loop for continuous improvement.

8. **Add Localization Considerations:**  
   - Show how text elements can be easily translated.  
   - Indicate where language selectors or region-based content may appear.

By following these steps, the next version of the text can evolve into a more comprehensive design document, offering not only stylistic and structural guidelines but also concrete interaction details, accessibility standards, and a clearer roadmap for developers and designers to implement the project successfully.