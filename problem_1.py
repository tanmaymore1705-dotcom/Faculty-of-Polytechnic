# ─────────────────────────────────────────────────────────────────────────────
# SUPERSEDED — KEPT FOR HISTORICAL PR REFERENCE
#
# This file is the original Day 1 problem and is preserved so existing student
# PR history remains valid. New submissions should go to:
#
#   lab/module_1_foundations/D01_seconds_in_week/
#
# See syllabus/COURSE_DESIGN.md for the active course plan.
# ─────────────────────────────────────────────────────────────────────────────

# Solve the following problem:
# Write a function to calculate the number of seconds in a week

# Write code here

def seconds_in_week():
    a = 60 # Secs in minute
    b = 60 * a # secs in an hour
    c = 24 * b # secs in a day
    d = 7 * c # secs in a week
    result = d
    return(result)

print(seconds_in_week())
