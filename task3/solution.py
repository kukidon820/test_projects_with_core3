
def appearance(intervals) -> int:
    lesson_start, lesson_end = intervals['lesson'][0], intervals['lesson'][1]

    def process_intervals(raw_intervals):
        processed = []
        pairs = [(raw_intervals[i], raw_intervals[i + 1]) for i in range(0, len(raw_intervals), 2)]
        for start, end in pairs:
            start = max(start, lesson_start)
            end = min(end, lesson_end)
            if start < end:
                processed.append((start, end))
        if not processed:
            return []
        processed.sort()
        merged = [processed[0]]
        for current_start, current_end in processed[1:]:
            last_start, last_end = merged[-1]
            if current_start <= last_end:
                new_start = last_start
                new_end = max(last_end, current_end)
                merged[-1] = (new_start, new_end)
            else:
                merged.append((current_start, current_end))
        return merged

    pupil_intervals = process_intervals(intervals['pupil'])
    tutor_intervals = process_intervals(intervals['tutor'])

    total_time = 0
    i = j = 0
    while i < len(pupil_intervals) and j < len(tutor_intervals):
        pupil_start, pupil_end = pupil_intervals[i]
        tutor_start, tutor_end = tutor_intervals[j]

        overlap_start = max(pupil_start, tutor_start)
        overlap_end = min(pupil_end, tutor_end)

        if overlap_start < overlap_end:
            total_time += overlap_end - overlap_start

        if pupil_end < tutor_end:
            i += 1
        else:
            j += 1

    return total_time


if __name__ == '__main__':
    tests = [
        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                       'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
         'answer': 3117},
        {'intervals': {'lesson': [1594702800, 1594706400],
                       'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                                 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                                 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                                 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                       'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
         'answer': 3577},
        {'intervals': {'lesson': [1594692000, 1594695600],
                       'pupil': [1594692033, 1594696347],
                       'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
         'answer': 3565},
    ]

    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])

        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
