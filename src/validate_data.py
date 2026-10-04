from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"

def check_courses(df):
    required = {"course_id","cohort_id","faculty_id","weekly_sessions",
                "duration_slots","required_room_type","students"}
    missing = required - set(df.columns)
    assert not missing, f"Missing course columns: {sorted(missing)}"
    assert df["course_id"].is_unique, "course_id values must be unique"
    assert (df["weekly_sessions"] >= 1).all() and (df["weekly_sessions"] <= 4).all(), "weekly_sessions must be 1-4"
    assert df["duration_slots"].isin([1,2]).all(), "duration_slots must be 1 or 2"
    assert df["required_room_type"].isin(["classroom","lab"]).all(), "Invalid room type"
    assert (df["students"] > 0).all(), "students must be positive"

def check_rooms(df):
    required = {"room_id","capacity","room_type"}
    missing = required - set(df.columns)
    assert not missing, f"Missing room columns: {sorted(missing)}"
    assert df["room_id"].is_unique, "room_id values must be unique"
    assert (df["capacity"] > 0).all(), "Room capacity must be greater than zero"
    assert df["room_type"].isin(["classroom","lab"]).all(), "Invalid room type"

def check_slots(df):
    required = {"slot_id","day","time","preferred"}
    missing = required - set(df.columns)
    assert not missing, f"Missing slot columns: {sorted(missing)}"
    assert df["slot_id"].is_unique, "slot_id values must be unique"
    assert df["preferred"].isin(["yes","no"]).all(), "preferred must be yes/no"

def main():
    courses = pd.read_csv(DATA / "courses.csv")
    rooms = pd.read_csv(DATA / "rooms.csv")
    slots = pd.read_csv(DATA / "timeslots.csv")

    print("courses:", courses.shape)
    print("rooms:", rooms.shape)
    print("timeslots:", slots.shape)

    check_courses(courses)
    check_rooms(rooms)
    check_slots(slots)

    # Cross-file checks
    room_types = set(rooms["room_type"])
    assert set(courses["required_room_type"]).issubset(room_types), "Course requires unavailable room type"
    print("STEP 1 DATA CHECK PASSED")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STEP 1 DATA CHECK FAILED")
        print("Reason:", e)
        raise SystemExit(1)
