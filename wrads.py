wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}
staff = {}

for field,docs in wards.items():
    for doctor in docs:
        staff['employees']={
            'names':doctor,
            'field':field
        }
print (staff)

