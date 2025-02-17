import datetime

import pytz
from django.utils import timezone


class DateTime:
    @staticmethod
    def get_available_time_slot_from_events_slots(
        event_slots: list[tuple[timezone.datetime, timezone.datetime]],
        start_time: timezone.datetime,
        end_time: timezone.datetime,
    ):
        ordered_time_slots = sorted(event_slots, key=lambda i: i[0])
        available_time_slots = []
        current_highest_end_time = None
        for id_, item in enumerate(ordered_time_slots):
            if id_ != 0:
                current_start_time = item[0]
                if current_start_time > current_highest_end_time:
                    available_time_slots.append(
                        (
                            current_highest_end_time + timezone.timedelta(seconds=1),
                            current_start_time - timezone.timedelta(seconds=1),
                        )
                    )
                    current_highest_end_time = None
                else:
                    ...
            end_time_ = item[1]
            if not current_highest_end_time:
                current_highest_end_time = end_time_
            elif end_time_ > current_highest_end_time:
                current_highest_end_time = end_time_
        if current_highest_end_time:
            available_time_slots.append(
                (current_highest_end_time + timezone.timedelta(seconds=1), end_time)
            )
        else:
            if available_time_slots:
                available_time_slots.append((available_time_slots[-1][1], end_time))
        lowest_start_time = available_time_slots[0][0]
        if lowest_start_time > start_time:
            available_time_slots = [
                (start_time, lowest_start_time - timezone.timedelta(seconds=1))
            ] + available_time_slots
        return available_time_slots

    @staticmethod
    def get_start_of_day(datetime: timezone.datetime):
        return datetime.replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def get_end_of_day(datetime: timezone.datetime):
        return datetime.replace(hour=23, minute=59, second=59)

    @staticmethod
    def check_if_time_is_at_the_end_of_the_day(time: datetime.time):
        return time.hour == 23 and time.minute == 59

    @staticmethod
    def check_if_time_is_at_the_start_of_the_day(time: datetime.time):
        return time.hour == 0 and time.minute == 0

    @staticmethod
    def get_end_of_working_day_in_current_week():
        targeted_end_of_week = 4
        now = timezone.datetime.now()
        offset_from_end_of_week_days = targeted_end_of_week - now.weekday()
        base_time = timezone.datetime(
            year=now.year,
            month=now.month,
            day=now.day,
            hour=17,
            minute=0,
            second=0,
            tzinfo=pytz.UTC,
        )
        if offset_from_end_of_week_days == 0:
            end_of_week = base_time
            if end_of_week > now:
                return end_of_week
            else:
                return end_of_week + timezone.timedelta(days=7)
        elif offset_from_end_of_week_days < 0:
            return (
                base_time
                + timezone.timedelta(days=offset_from_end_of_week_days)
                + timezone.timedelta(days=7)
            )

        else:
            return base_time + timezone.timedelta(days=offset_from_end_of_week_days)
