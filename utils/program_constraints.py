from utils.datetime_helper import from_string_to_datetime, get_time_difference_in_minutes

"""
Validates whether the current conference program meets the constraints for the program.

- `program`: The conference program to validate. It must adhere to the JSON format described in the README.md.
- `num_conference_sessions`: The number of conference sessions in the conference.
- `num_parallel_tracks`: The number of parallel tracks in the conference.
- `session_len`: The length of each session.
"""
def validate_conference_program(program={}, num_conference_sessions=1, num_parallel_tracks=1, session_len=60):
    assert("sessions" in program)
    # Total number of sessions has to be equal to the number of sessions provided by the PC chairs.
    assert(len(program["sessions"]) == num_conference_sessions)
    for session in program["sessions"]:
        assert("id" in session)
        assert("tracks" in session)

        busy_people = {}
        assert(len(session["tracks"]) <= num_parallel_tracks)
        for track in session["tracks"]:
            assert("name" in track)
            assert("talks" in track)
            assert("startTime" in track)
            assert("endTime" in track)

            listed_track_duration = get_time_difference_in_minutes(track["startTime"], track["endTime"])
            assert(listed_track_duration <= session_len)

            earliest_talk_time = from_string_to_datetime(track["talks"][-1]["endTime"])
            latest_talk_time = from_string_to_datetime(track["talks"][0]["startTime"])
            for talk in track["talks"]:
                assert("name" in talk)
                assert("abstract" in talk)
                assert("topics" in talk)
                assert("authors" in talk)
                assert("startTime" in talk)
                assert("endTime" in talk)

                for a in talk["authors"]:
                    author_name = a["name"]
                    if author_name not in busy_people:
                        busy_people[author_name] = []

                    busy_people[author_name].append((talk["startTime"], talk["endTime"]))
                
                earliest_talk_time = min(earliest_talk_time, from_string_to_datetime(talk["startTime"]))
                latest_talk_time = max(latest_talk_time, from_string_to_datetime(talk["endTime"]))

            # Total time for all presentations in a session cannot be longer than the length of the session.
            assert(get_time_difference_in_minutes(earliest_talk_time, latest_talk_time) <= session_len)

        # If there are parallel tracks, then no two papers with common authors can be scheduled in parallel at the same time.
        for p in busy_people:
            busy_times = busy_people[p]
            busy_times.sort(key=lambda x: x[0])

            for i in range(1, len(busy_times)):
                assert(busy_times[i][0] >= busy_times[i-1][1])
