def create_report(title, *sections, **metadata):
    """Create a report: report title, sections in string and metadata"""
    return {'report_title': title, 'report_sections': list(sections), **metadata}

def summarize_report(report):
    sections_lines = "\nSections: \n"
    for section in report['report_sections']:
        sections_lines += f"{section} \n"

    metadata_lines = "\nMetadata: \n"
    for key, value in report.items():
        if key not in ('report_title', 'report_sections'):
            metadata_lines += f"{key}: {value}\n"

    return f"{report['report_title']} \n{sections_lines} {metadata_lines}"

def count_words(*sections):
    word_count = 0;
    for section in sections:
        if isinstance(section, str):
            word_count += len(section.split())
    return word_count

# --- Main like section ---
report_a = create_report(
    "Q3 Summary",
    'section1 and more',
    'section2',
    author = 'Johanna',
    department = 'Development',
    version = '1.0',
    date = '2026-09-15'
    )

print(summarize_report(report_a))

print(count_words(*report_a['report_sections']))

metadata_dev = {
    'author': 'Johanna',
    'department': 'Development',
    'version': '1.0',
    'date': '2026-09-15'
}

metadata_hr = {
    'author': 'Anna',
    'department': 'HR',
    'confidential': True
}

report_dev = create_report(
    "Development Summary",
    "Initial planning completed",
    "Sprint 1 delivered",
    **metadata_dev
)

report_hr = create_report(
    "HR Policy Update",
    "New guidelines introduced",
    **metadata_hr
)

report_missing = create_report(
    "System Overview",
    "All systems operational.",
    author="Markus"
)

print(report_missing.get('version', "No version provided"))