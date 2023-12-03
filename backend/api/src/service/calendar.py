from data.oneshot_table import OneShotDB
from model.date import CalendarEntryRespDTO, MonthDTO
from model.oneshot import OneShotRespDTO
from model.user import UserDTO

os_db = OneShotDB()


class CalendarService:
    async def get_calendar(
        self, user: UserDTO, month: MonthDTO
    ) -> list[CalendarEntryRespDTO]:
        oneshots = await os_db.get_calendar_month(user.username, month)
        return [
            CalendarEntryRespDTO(oneshot=OneShotRespDTO.from_db_oneshot(i), date=i.date)
            for i in oneshots
        ]
