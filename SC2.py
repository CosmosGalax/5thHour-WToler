#Name:Wyatt toler
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI
import math
#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
PatientWeightLb = float(input("Enter Patient's Weight(lbs): "))
PatientHeight = (input("Enter Patient's Height(Feet'Inch): "))
Feet, Inch, = PatientHeight.split("'")
PatientHeightFeet = (int(Inch)) + (int(Feet) * 12)
PatientBMI = (PatientWeightLb / (PatientHeightFeet ** 2)) * 703

if PatientBMI > 30:
    print("You are Obese your BMI is", round(PatientBMI, 1))
elif 25 <= PatientBMI <= 29.9:
    print("You are OverWeight your BMI is", round(PatientBMI, 1))
elif 18.5 <= PatientBMI <= 24.9:
    print("You are Normal Weight your BMI is", round(PatientBMI, 1))
else:
    print("You are Underweight your BMI is", round(PatientBMI, 1))
print("Thank you for using our BMI Calculator!")
