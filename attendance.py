import copy

# Tested on Python 3.8.6
# Replace the sample list below with any.

# noinspection SpellCheckingInspection
attendanceList = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole'],
    ['Brad', 'Walter', 'Sam', 'Krish', 'Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer', 'Desmond', 'Harry', 'Nicole', 'Sam'],
]


def get_daily_participants(daily_attendance: list):
    """
    Returns participants who attended daily.

    :param daily_attendance: list
    :return: list
    """
    first_day_participants = []
    if daily_attendance:
        first_day_participants = copy.deepcopy(daily_attendance[0])

    for day in daily_attendance:
        for participant in first_day_participants:
            # If participant missed once, remove them from list
            if participant not in day:
                first_day_participants.remove(participant)
                continue

    return first_day_participants


def get_once_participants(daily_attendance: list):
    """
    Returns participants who attended only once.

    :param daily_attendance: list
    :return: list
    """

    once_participants = []
    for day in range(len(daily_attendance)):
        unique = [*set(daily_attendance[day]).difference(*daily_attendance[:day], *daily_attendance[day + 1:])]
        # If unique item exist, keep them
        if unique:
            once_participants += unique

    return once_participants


def get_first_day_participants(daily_attendance: list):
    """
    Returns participants who attended only on first day.

    :param daily_attendance: list
    :return: list
    """
    first_day_participants = []
    attendance = copy.deepcopy(daily_attendance)

    if attendance:
        first_day_participants = attendance.pop(0)

    for day in attendance:
        for participant in first_day_participants:
            # If participant came back, remove them from list
            if participant in day:
                first_day_participants.remove(participant)
                continue

    return first_day_participants


print("Daily: " + str(get_daily_participants(attendanceList)))
print("Once: " + str(get_once_participants(attendanceList)))
print("First day only: " + str(get_first_day_participants(attendanceList)))
