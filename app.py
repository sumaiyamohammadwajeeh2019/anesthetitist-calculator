#!/usr/bin/env python3
"""Anaesthetist Calculator - Python Implementation
Developed by Dr.Sumaiya Mohammad (SMRR Team), Bangladesh
"""

import sys

# EXPANDED COMPANIES DATABASE (includes Ibn Sina)
COMPANIES = [
    'Square',       # 0
    'Incepta',      # 1
    'Beximco',      # 2
    'Renata',       # 3
    'ACI',          # 4
    'Opsonin',      # 5
    'Eskayef',      # 6
    'Ibn Sina',     # 7 - Added Ibn Sina pharmaceuticals
]

# DRUG DATABASE with Company-Specific Names and Prices
# Format: each drug has prices for all 8 companies (indices 0-7)
DRUGS = [
    {"generic": "Propofol 1% 200mg/20ml", "class": "IV anaesthetic", "dose": "Induction 2-2.5 mg/kg IV; Maint 100-200 mcg/kg/min",
     "indication": "Induction/maintenance of GA; ICU sedation",
     "contraindication": "Egg/soy allergy; hemodynamic instability; raised ICP",
     "prices": [180, 165, 170, 190, 175, 160, 185, 170]},  # + Ibn Sina price
    {"generic": "Ketamine 50mg/ml 10ml", "class": "IV anaesthetic", "dose": "1-2 mg/kg IV; 4-6 mg/kg IM",
     "indication": "Induction; analgesia; procedural sedation",
     "contraindication": "Raised ICP; psychosis; uncontrolled HTN; glaucoma",
     "prices": [120, 110, 115, 130, 125, 105, 128, 115]},
    {"generic": "Thiopental Na 500mg", "class": "IV anaesthetic", "dose": "3-5 mg/kg IV",
     "indication": "Induction of GA",
     "contraindication": "Porphyria; asthma; CV instability; airway obstruction",
     "prices": [90, 85, 88, 95, 92, 80, 93, 88]},
    {"generic": "Etomidate 20mg/10ml", "class": "IV anaesthetic", "dose": "0.2-0.3 mg/kg IV",
     "indication": "Induction in hemodynamically unstable",
     "contraindication": "Adrenal insufficiency; sepsis (relative)",
     "prices": [450, 430, 440, 460, 435, 420, 455, 440]},
    {"generic": "Midazolam 5mg/5ml", "class": "Benzodiazepine", "dose": "0.02-0.1 mg/kg IV; 0.5-0.7 mg/kg PO (ped)",
     "indication": "Anxiolysis; sedation; premedication",
     "contraindication": "Acute narrow-angle glaucoma; shock; myasthenia",
     "prices": [60, 55, 58, 65, 62, 52, 63, 58]},
]

# ADDITIONAL DRUGS (continuing from index 5 onwards)


def list_drugs():
    """List all drugs with company names and prices."""
    lines = []
    for i, drug in enumerate(DRUGS):
        price_info = []
        for j in range(min(3, len(COMPANIES))):
            price_info.append(f"{COMPANIES[j]}: {drug['prices'][j]} BDT")
        price_info.append(f"Ibn Sina: {drug['prices'][7]} BDT")
        lines.append(f"{i}. {drug['generic']} | {' | '.join(price_info)}")
    return "\n".join(lines)


def main():
    """Run the 8-in-1 Anaesthetist Calculator with Price Update."""
    print("=" * 60)
    print("Global Anaesthetic Calculator & Ibn Sina Medicine Database")
    print("=" * 60)
    print("Developed by Dr.Sumaiya Mohammad (SMRR Team), Bangladesh")
    print("Includes Ibn Sina Pharmaceuticals pricing")
    print("Price update functionality enabled")
    while True:
        print("Select Calculator:")
        print("1. Spinal Anesthesia Dosage")
        print("2. Local Anesthetic Max Dose")
        print("3. Burn Resuscitation (Parkland Formula)")
        print("4. Vitals Reference Ranges")
        print("5. Drug Price Lookup with Updates")
        print("6. List All Drugs with Companies")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()
        if choice == "1":
            try:
                weight = float(input("Patient weight (kg): "))
                print(f"\nSpinal Anesthesia Dosage:\n{calculate_spinal_anesthesia(weight)}\n")
            except ValueError:
                print("Please enter a valid weight.\n")
        elif choice == "2":
            try:
                weight = float(input("Patient weight (kg): "))
                print("\nLocal Anesthetics available:")
                for la in ["Articaine", "Mepivacaine", "Prilocaine", "Chloroprocaine", "Tetracaine"]:
                    print(f"  - {la}")
                la_name = input("Enter local anesthetic name: ").strip()
                print(f"\n{calculate_local_anesthetic(weight, la_name)}\n")
            except ValueError:
                print("Please enter a valid weight.\n")
        elif choice == "3":
            try:
                weight = float(input("Patient weight (kg): "))
                percentage = float(input("Burn percentage (%TBSA): "))
                time = float(input("Time since burn (hours): "))
                print(f"\nBurn Resuscitation:\n{calculate_parkland_formula(weight, percentage, time)}\n")
            except ValueError:
                print("Please enter valid numbers.\n")
        elif choice == "4":
            print(f"\n{calculate_vitals()}\n")
        elif choice == "5":
            print("\nDrug Price Lookup with Updates:")
            print("\nDrug Index (first 10):")
            for i, drug in enumerate(DRUGS[:10]):
                print(f"  {i}: {drug['generic']}")
            try:
                drug_idx = int(input("Enter drug index: "))
                company_idx = int(input(f"Enter company index (0-{len(COMPANIES)-1}, Ibn Sina={len(COMPANIES)-1}): "))
                print("\nOptions:")
                print("  1. Show current price")
                print("  2. Update market price")
                print("  3. Both show and update")
                sub_choice = input("Enter option (1-3): ").strip()
                if sub_choice == "1":
                    print(f"\n{calculate_drug_price(drug_idx, company_idx)}\n")
                elif sub_choice == "2":
                    try:
                        new_price = int(input("Enter new market price (BDT): "))
                        print(f"\n{calculate_drug_price_updated(drug_idx, company_idx, new_price)}\n")
                    except ValueError:
                        print("Invalid price entered.\n")
                elif sub_choice == "3":
                    try:
                        new_price = int(input("Enter new market price (BDT): "))
                        print(f"\n{calculate_drug_price_updated(drug_idx, company_idx, new_price)}\n")
                    except ValueError:
                        print("Invalid price entered.\n")
                else:
                    print("Invalid option.\n")
            except (ValueError, IndexError):
                print("Invalid input.\n")
        elif choice == "6":
            print(f"\n{list_drugs()}\n")
        elif choice == "7":
            print("\nGoodbye! 🌟💊\n")
            break
        else:
            print("Invalid choice. Please enter 1-7.\n")


if __name__ == "__main__":
    main()
\ndef calculate_spinal_anesthesia(weight_kg):
    \"\"\"Spinal anesthesia dosage calculation.
    Spinal: 0.3-0.5 mg/kg
    Adult: 12-15 mg
    Caudal (0.25%): 1 ml/kg
    \"\"\"
    min_dose = 0.3 * weight_kg
    max_dose = 0.5 * weight_kg
    adult_min = 12
    adult_max = 15
    caudal_ml = weight_kg
    return f\"Spinal: {min_dose:.1f}-{max_dose:.1f} mg\\nAdult: {adult_min}-{adult_max} mg\\nCaudal 0.25%: {caudal_ml} ml\"

\ndef calculate_local_anesthetic(weight_kg, drug_name):
    \"\"\"Local anesthetic maximum dose calculation.\"
    limits = {\"Articaine\": 7, \"Mepivacaine\": 4.4, \"Prilocaine\": 6, \"Chloroprocaine\": 11, \"Tetracaine\": 1.5}
    if drug_name not in limits:
        return f\"Unknown local anesthetic: {drug_name}\"
    max_mg = weight_kg * limits[drug_name]
    note = \" (Max 6.6 mg/kg with adren)\" if drug_name == \"Mepivacaine\" else \"\"
    return f\"{drug_name} Max dose: {max_mg:.1f} mg{note}\"

\ndef calculate_parkland_formula(weight_kg, burn_percentage, time_since_burn):
    \"\"\"Parkland burn resuscitation formula.
    Total 24h fluid = 4 ml * weight(kg) * %TBSA
    \"\"\"
    total_24h = 4 * weight_kg * burn_percentage
    first_8h = total_24h / 2
    next_16h = total_24h / 2
    brooke = 2 * weight_kg * burn_percentage
    return f\"Parkland 24h: {total_24h:.0f} ml (4 ml/kg/%TBSA)\\nBrooke 24h: {brooke:.0f} ml\\n1st 8h: {first_8h:.0f} ml\\nnext 16h: {next_16h:.0f} ml\"

\ndef calculate_vitals():
    \"\"\"Vitals reference ranges.\"\"\"
    return \"Vitals Reference Ranges:\\nNeonate: HR 120-160 | SBP 60-80 | RR 40-60\\n1-12 months: HR 100-150\\n1-10 years: HR 80-130 | SBP 90+(2×age)\\nAdult: HR 60-100 | MAP >65\"

\ndef calculate_drug_price(drug_index, company_index):
    \"\"\"Calculate drug price from the database.\"\"\"
    if drug_index < 0 or drug_index >= len(DRUGS):
        return \"Invalid drug index\"
    if company_index < 0 or company_index >= len(COMPANIES):
        return \"Invalid company index\"
    drug = DRUGS[drug_index]
    price = drug[\"p\"][company_index]
    if price == 0:
        return \"Price not available\"
    usd = price / 110
    inr = price / 1.32
    kwd = price / 358
    rial = price / 29.3
    eur = price / 120
    return f\"BDT: {price}\\nUSD: {usd:.2f}\\nINR: {inr:.2f}\\nKWD: {kwd:.3f}\\nRial: {rial:.2f}\\nEUR: {eur:.2f}\"

\ndef list_drugs():
    \"\"\"List all drugs in the database.\"\"\"
    lines = []
    for i, drug in enumerate(DRUGS):
        prices = drug[\"p\"]
        lines.append(f\"{i}. {drug['name']} | {drug['cls']} | Dose: {drug['dose']} | Indication: {drug['ind'][:30]}...\")
    return \"\\n\".join(lines)
\ndef main():
    \"\"\"Run the 8-in-1 Anaesthetist Calculator CLI.\"\"\"
    print(\"=\" * 60)
    print(\"\\u2695 Global Anaesthetic Calculator & Medicine Database\")
    print(\"=\" * 60)
    print(\"Developed by Dr.Sumaiya Mohammad (SMRR Team), Bangladesh\")
    print()
    while True:
        print(\"Select Calculator:\")
        print(\"1. Spinal Anesthesia Dosage\")
        print(\"2. Local Anesthetic Max Dose\")
        print(\"3. Burn Resuscitation (Parkland Formula)\")
        print(\"4. Vitals Reference Ranges\")
        print(\"5. Drug Price Lookup\")
        print(\"6. List All Drugs\")
        print(\"7. Exit\")
        print()
        choice = input(\"Enter choice (1-7): \").strip()
        if choice == \"1\":
            try:
                weight = float(input(\"Patient weight (kg): \"))
                result = calculate_spinal_anesthesia(weight)
                print(f\"\\nSpinal Anesthesia Dosage:\\n{result}\\n\")
            except ValueError:
                print(\"Please enter a valid weight.\\n\")
        elif choice == \"2\":
            try:
                weight = float(input(\"Patient weight (kg): \"))
                print(\"\\nLocal Anesthetics available:\")
                for la in [\"Articaine\", \"Mepivacaine\", \"Prilocaine\", \"Chloroprocaine\", \"Tetracaine\"]:
                    print(f\"  - {la}\")
                la_name = input(\"Enter local anesthetic name: \").strip()
                result = calculate_local_anesthetic(weight, la_name)
                print(f\"\\n{result}\\n\")
            except ValueError:
                print(\"Please enter a valid weight.\\n\")
        elif choice == \"3\":
            try:
if __name__ == "__main__":
    main()
                weight = float(input(\"Patient weight (kg): \"))
                percentage = float(input(\"Burn percentage (%TBSA): \"))
                time = float(input(\"Time since burn (hours): \"))
                result = calculate_parkland_formula(weight, percentage, time)
                print(f\"\\nBurn Resuscitation:\\n{result}\\n\")
            except ValueError:
                print(\"Please enter valid numbers.\\n\")
        elif choice == \"4\":
            result = calculate_vitals()
            print(f\"\\n{result}\\n\")
        elif choice == \"5\":
            print(\"\\nDrug Index (first 10):\")
            for i, drug in enumerate(DRUGS[:10]):
                print(f\"  {i}: {drug['name']}\")
            try:
                drug_idx = int(input(\"Enter drug index: \"))
                company_idx = int(input(\"Enter company index (0-6): \"))
                result = calculate_drug_price(drug_idx, company_idx)
                print(f\"\\nDrug Price:\\n{result}\\n\")
            except (ValueError, IndexError):
                print(\"Invalid input.\\n\")
        elif choice == \"6\":
            print(f\"\\n{list_drugs()}\\n\")
        elif choice == \"7\":
            print(\"\\nGoodbye! \\u2728\\n\")
            break
        else:
            print(\"Invalid choice. Please enter 1-7.\\n\")

if __name__ == \"__main__\":
    main()
