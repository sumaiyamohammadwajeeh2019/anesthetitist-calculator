#!/usr/bin/env python3
"""Anaesthetist Calculator and Medicine Database - Developed by Dr.Sumaiya Mohammad (SMRR Team)"""

COMPANIES = ['Square','Incepta','Beximco','Renata','ACI','Opsonin','Eskayef','Ibn Sina']

DRUGS = [
    {"generic": "Propofol 1% 200mg/20ml", "class": "IV anaesthetic", "dose": "Induction 2-2.5 mg/kg IV", "indication": "Induction/maintenance of GA", "contraindication": "Egg/soy allergy", "prices": [180,165,170,190,175,160,185,170]},
    {"generic": "Ketamine 50mg/ml 10ml", "class": "IV anaesthetic", "dose": "1-2 mg/kg IV; 4-6 mg/kg IM", "indication": "Induction; analgesia", "contraindication": "Raised ICP; psychosis", "prices": [120,110,115,130,125,105,128,115]},
    {"generic": "Thiopental Na 500mg", "class": "IV anaesthetic", "dose": "3-5 mg/kg IV", "indication": "Induction of GA", "contraindication": "Porphyria; asthma", "prices": [90,85,88,95,92,80,93,88]},
    {"generic": "Etomidate 20mg/10ml", "class": "IV anaesthetic", "dose": "0.2-0.3 mg/kg IV", "indication": "Induction in unstable patient", "contraindication": "Adrenal insufficiency", "prices": [450,430,440,460,435,420,455,440]},
    {"generic": "Midazolam 5mg/5ml", "class": "Benzodiazepine", "dose": "0.02-0.1 mg/kg IV", "indication": "Sedation; premedication", "contraindication": "Glaucoma; shock", "prices": [60,55,58,65,62,52,63,58]},
]

def calculate_spinal_anesthesia(weight_kg):
    min_dose = 0.3 * weight_kg
    max_dose = 0.5 * weight_kg
    return f"Spinal: {min_dose:.1f}-{max_dose:.1f} mg\nAdult: 12-15 mg\nCaudal 0.25%: {weight_kg:.0f} ml"

def calculate_local_anesthetic(weight_kg, drug_name):
    limits = {"Articaine": 7, "Mepivacaine": 4.4, "Prilocaine": 6, "Chloroprocaine": 11, "Tetracaine": 1.5}
    if drug_name not in limits:
        return f"Unknown local anesthetic: {drug_name}"
    max_mg = weight_kg * limits[drug_name]
    note = " (Max 6.6 mg/kg with adren)" if drug_name == "Mepivacaine" else ""
    return f"{drug_name} Max dose: {max_mg:.1f} mg{note}"

def calculate_parkland_formula(weight_kg, burn_percentage, time_since_burn):
    total_24h = 4 * weight_kg * burn_percentage
    first_8h = total_24h / 2
    next_16h = total_24h / 2
    brooke = 2 * weight_kg * burn_percentage
    return f"Parkland 24h: {total_24h:.0f} ml (4 ml/kg/%TBSA)\nBrooke 24h: {brooke:.0f} ml\n1st 8h: {first_8h:.0f} ml\nNext 16h: {next_16h:.0f} ml\nTime since burn: {time_since_burn}h"

def calculate_vitals():
    return "Vitals Reference Ranges:\nNeonate: HR 120-160 | SBP 60-80 | RR 40-60\n1-12 months: HR 100-150\n1-10 years: HR 80-130 | SBP 90+(2xage)\nAdult: HR 60-100 | MAP >65"

def calculate_drug_price(drug_index, company_index):
    if drug_index < 0 or drug_index >= len(DRUGS):
        return "Invalid drug index"
    if company_index < 0 or company_index >= len(COMPANIES):
        return "Invalid company index"
    drug = DRUGS[drug_index]
    price = drug["prices"][company_index]
    if price == 0:
        return "Price not available"
    usd = price / 110
    inr = price / 1.32
    kwd = price / 358
    rial = price / 29.3
    eur = price / 120
    return f"{drug['generic']} - {COMPANIES[company_index]}\nBDT: {price}\nUSD: {usd:.2f}\nINR: {inr:.2f}\nKWD: {kwd:.3f}\nRial: {rial:.2f}\nEUR: {eur:.2f}"

def calculate_drug_price_updated(drug_index, company_index, new_price):
    if drug_index < 0 or drug_index >= len(DRUGS):
        return "Invalid drug index"
    if company_index < 0 or company_index >= len(COMPANIES):
        return "Invalid company index"
    DRUGS[drug_index]["prices"][company_index] = new_price
    return f"Updated! {DRUGS[drug_index]['generic']} - {COMPANIES[company_index]} = {new_price} BDT"

def list_drugs():
    lines = []
    for i, drug in enumerate(DRUGS):
        lines.append(f"{i}. {drug['generic']} | {drug['class']} | Dose: {drug['dose']} | Ibn Sina: {drug['prices'][7]} BDT")
    return "\n".join(lines)

def main():
    print("=" * 60)
    print("Global Anaesthetic Calculator & Ibn Sina Medicine Database")
    print("Developed by Dr.Sumaiya Mohammad (SMRR Team), Bangladesh")
    print("=" * 60)
    while True:
        print("\nSelect Calculator:")
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
            print("\nDrug Index:")
            for i, drug in enumerate(DRUGS):
                print(f"  {i}: {drug['generic']}")
            try:
                drug_idx = int(input("Enter drug index: "))
                company_idx = int(input(f"Enter company index (0-{len(COMPANIES)-1}, Ibn Sina={len(COMPANIES)-1}): "))
                print("\nOptions:\n  1. Show current price\n  2. Update market price\n  3. Both show and update")
                sub = input("Enter option (1-3): ").strip()
                if sub == "1":
                    print(f"\n{calculate_drug_price(drug_idx, company_idx)}\n")
                elif sub == "2":
                    new_price = int(input("Enter new market price (BDT): "))
                    print(f"\n{calculate_drug_price_updated(drug_idx, company_idx, new_price)}\n")
                elif sub == "3":
                    new_price = int(input("Enter new market price (BDT): "))
                    print(f"\n{calculate_drug_price_updated(drug_idx, company_idx, new_price)}\n")
                else:
                    print("Invalid option.\n")
            except (ValueError, IndexError):
                print("Invalid input.\n")
        elif choice == "6":
            print(f"\n{list_drugs()}\n")
        elif choice == "7":
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice. Please enter 1-7.\n")

if __name__ == "__main__":
    main()
