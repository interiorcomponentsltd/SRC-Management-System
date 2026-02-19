# Spirit Realm Centre - Church Management System v2.0

## Overview
A fully-featured, browser-based church management system for managing members, attendance, cell churches, and departmental operations. Built with React 18 (UMD) and deployed as a single HTML file.

## Key Features  
✅ **Member Management**
- Import and auto-populate 1000+ members from Excel extracts
- Add, search, and filter members by name/phone/department
- Normalize and map unmapped members to departments
- Track first-timers for follow-up

✅ **Department & Leadership**
- 10+ departments with independent login credentials
- Department-wise member assignment
- Admin access with full view across all departments
- Department leader restricted to their department

✅ **Attendance Tracking**
- Record attendance per department
- Bulk import from Excel files
- Automated mark present/absent from pasted member names
- Historical attendance records

✅ **Cell Churches**
- Create and manage cell church groups
- Assign leaders and meeting times
- Track members per group
- Edit/delete groups

✅ **First Timers Follow-up**
- Dedicated tracking for first-time visitors  
- Prayer requests and inviter information
- Search and export for follow-up campaigns

✅ **Analytics & Reports**
- Member statistics by department
- Attendance trends
- Member gender/status breakdown
- Export data to Excel

✅ **Audit & Mappings**
- Review unmapped member-to-department assignments
- Auto-suggest mappings based on member names
- Bulk apply suggestions with preview
- Undo last mapping action
- Full audit log with export to JSON

## Files Structure
```
index.html                      # Main application (single-file React App)
app_data.js                     # Department credentials and fallback hardcoded members
general_members.json            # Extracted general members (~1000+)
first_timers_followup.json      # Extracted first-timer records (~98)
spirit realm centre logo.jpg    # Church logo (used in UI)
```

## Getting Started

### 1. **Local Setup (Development)**
```bash
# Navigate to the project folder
cd "c:\Users\barth\OneDrive\Desktop\SRC ATTENDANCE ADMIN\src-mgt-sys"

# Start local HTTP server (Python 3)
python -m http.server 8000 --directory .

# Open browser and navigate to
http://localhost:8000/index.html
```

### 2. **Web Server Deployment (Production)**
Copy all files to your web server (Apache, Nginx, IIS, etc.):
- `index.html`
- `app_data.js`
- `general_members.json`
- `first_timers_followup.json`
- `spirit realm centre logo.jpg`

**Important**: Ensure CORS headers are set if serving from different domain.

### 3. **First Login**
Department credentials are stored in `app_data.js`. Default access:
- **Admin**: username=`admin` password=`SRC2024admin`
- **Any Department**: select department → enter password (e.g., `SRC2024menofimpact` for Men of Impact)

## User Roles

### **Admin**
- View all departments and members
- Manage all attendance records
- Access department credentials page
- View and edit all cell churches
- Full analytics access

### **Department Leader**
- View only members in assigned department
- Record attendance for department
- Create/manage cell churches within department
- View department-specific analytics

## Core Pages

| Page | Purpose | Access |
|------|---------|--------|
| Dashboard | Summary stats and recent members | All |
| Members | Browse/search all members, add new | All |
| First Timers | Track and follow up first-time visitors | All |
| Cell Churches | Manage home groups/cells | All |
| Attendance | Manual attendance recording | All |
| Bulk Attendance | Paste member names to mark present/absent | All |
| Upload Attendance | Import attendance from Excel file | All |
| Mappings | Review & assign unmapped members to departments | Admin |
| Departments | View/manage department credentials | Admin |
| Analytics | Statistics and member breakdown reports | All |

## Data Import & Normalization

### Imported Data
- **general_members.json**: Members extracted from "SPIRIT REALM CENTRE SUNDAYS ATTENDANCE TRACKER.xlsx"
- **first_timers_followup.json**: First-timers extracted from "FIRST TIMERS NEW MEMBERS1.xlsx"

### Automatic Processing
1. **Normalization**: Names and phone numbers cleaned and standardized
2. **Department Mapping**: Member departments are mapped to 10 canonical departments:
   - Men of Impact
   - Women of Purpose
   - Music House
   - Ushers
   - Security
   - Sanctuary
   - Prayer Group
   - Media
   - Godly Action
   - Counseling

3. **Duplicate Handling**: Members with same phone dedup'd; IDs auto-assigned

### Manual Mapping
Use **Mappings** page to:
1. Review unmapped members
2. Auto-suggest best-fit departments
3. Manually assign members
4. Preview and apply bulk changes
5. Undo last mapping if needed

## Data Persistence

### Local Storage
- `src_members_v2`: Members list (synced with imports)
- `src_attendance_v2`: Attendance records
- `src_cell_churches`: Cell church groups
- `mapping_history`: Audit log of mapping changes

### First Load Behavior
On first load, the app imports `general_members.json` and `first_timers_followup.json` and syncs them to localStorage. Subsequent edits persist to localStorage.

## Backup & Recovery

### Export Data
1. **Members**: Use Export Excel button on Members page
2. **Attendance**: Use Export Excel on Attendance pages
3. **Mapping Audit**: Use Export Audit Log on Mappings page

### Restore Data
1. Clear localStorage: Press F12 → Application → Clear all
2. Reload page: Browser will re-import from JSON files

## Troubleshooting

### Members not appearing
- Check browser console (F12) for JSON load errors
- Ensure `general_members.json` and `first_timers_followup.json` exist
- Clear localStorage and reload

### Search not finding members
- Use normalized search (ignores punctuation, extra spaces)
- Try partial name or phone number
- Check spelling

### Department login fails
- Verify department name exactly matches dropdown
- Check password in `app_data.js` for that department

### Mappings not saving
- Ensure localStorage is enabled in browser
- Check browser quota (usually > 5MB available)

## Security Notes
⚠️ **Not for production without HTTPS**
- This is a client-side app; credentials are visible in JS
- Deploy on HTTPS-only servers
- Consider adding database backend for sensitive deployments

## Browser Support
- Chrome/Edge/Firefox (latest versions)
- Mobile browsers supported (responsive design)
- Requires JavaScript enabled

## Future Enhancements
- Backend database integration (MySQL/PostgreSQL)
- User authentication with hashing
- Multi-church support
- Mobile app (React Native)
- Email/SMS notifications
- Budget tracking
- Event management

## Support & Maintenance
For issues or feature requests:
1. Check GitHub repo: https://github.com/interiorcomponentsltd/SRC-Management-System
2. Review existing issues and PRs
3. Create a new issue with details

---

**Version**: 2.0 | **Last Updated**: February 2026 | **Status**: Production Ready
