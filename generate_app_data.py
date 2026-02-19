#!/usr/bin/env python3
"""Generate app_data.js with extracted members and department authentication."""

import json

# Department credentials
DEPARTMENTS = {
    'Men of Impact': {
        'username': 'menofimpact',
        'password': 'SRC2024menofimpact',
        'description': 'Men of Impact Ministry'
    },
    'Women of Purpose': {
        'username': 'womenofpurpose',
        'password': 'SRC2024womenofpurpose',
        'description': 'Women of Purpose Ministry'
    },
    'Music House': {
        'username': 'musichouse',
        'password': 'SRC2024musichouse',
        'description': 'Music & Worship'
    },
    'Ushers': {
        'username': 'ushers',
        'password': 'SRC2024ushers',
        'description': 'Ushering Ministry'
    },
    'Security': {
        'username': 'security',
        'password': 'SRC2024security',
        'description': 'Security Ministry'
    },
    'Sanctuary': {
        'username': 'sanctuary',
        'password': 'SRC2024sanctuary',
        'description': 'Sanctuary Ministry'
    },
    'Prayer Group': {
        'username': 'prayergroup',
        'password': 'SRC2024prayergroup',
        'description': 'Prayer Group'
    },
    'Media': {
        'username': 'media',
        'password': 'SRC2024media',
        'description': 'Media & Tech Ministry'
    },
    'Godly Action': {
        'username': 'godlyaction',
        'password': 'SRC2024godlyaction',
        'description': 'Godly Action Ministry'
    },
    'Counseling': {
        'username': 'counseling',
        'password': 'SRC2024counseling',
        'description': 'Counseling Ministry'
    },
    'admin': {
        'username': 'admin',
        'password': 'SRC2024admin',
        'description': 'Administrator (Full Access)'
    }
}

# Read extracted members
with open('extracted_members.json', 'r') as f:
    members = json.load(f)

# Count stats
total_members = len(members)
departments_data = {}
for member in members:
    dept = member.get('department', 'Unassigned')
    if dept not in departments_data:
        departments_data[dept] = []
    departments_data[dept].append(member)

# Generate JavaScript code
js_code = f"""// Spirit Realm Centre - Church Management System Data
// Auto-generated: {total_members} members from Excel extraction

// Department Login Credentials
const DEPARTMENTS = {json.dumps(DEPARTMENTS, indent=2)};

// All Members Data ({total_members} total)
const MEMBERS = {json.dumps(members, indent=2)};

// Department-specific member lists
const DEPARTMENT_MEMBERS = {{"""

for dept in sorted(DEPARTMENTS.keys()):
    if dept == 'admin':
        continue
    dept_members = departments_data.get(dept, [])
    member_ids = [m['id'] for m in dept_members]
    js_code += f"\n    '{dept}': {json.dumps(member_ids)},"

js_code += """
};

// Cell Church Groups (for group-based organization)
const CELL_CHURCHES = [
    {
        id: 1,
        name: 'Sample Cell Group 1',
        location: 'Benin City',
        leader: 'Church Leader',
        members: [1, 2, 3, 4, 5],
        meeting_day: 'Wednesday',
        meeting_time: '6:30 PM'
    }
];

// Attendance Records
const ATTENDANCE_RECORDS = [];

// System Configuration
const CONFIG = {
    app_name: 'Spirit Realm Centre - Management System',
    version: '2.0.0',
    church_name: 'Spirit Realm Centre',
    default_page: 'dashboard',
    total_members: """ + str(total_members) + """,
    total_departments: """ + str(len([d for d in DEPARTMENTS if d != 'admin'])) + """
};

// Export for use in app
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { DEPARTMENTS, MEMBERS, DEPARTMENT_MEMBERS, CELL_CHURCHES, ATTENDANCE_RECORDS, CONFIG };
}
"""

# Write the JavaScript file
with open('app_data.js', 'w') as f:
    f.write(js_code)

print("✓ Generated app_data.js with:")
print(f"  - {total_members} members")
print(f"  - {len([d for d in DEPARTMENTS if d != 'admin'])} departments")
for dept in sorted(DEPARTMENTS.keys()):
    if dept != 'admin':
        count = len(departments_data.get(dept, []))
        print(f"    • {dept}: {count} members")
