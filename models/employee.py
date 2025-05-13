from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    email: str
    name: str
    department: str
    hours_worked: float
    hourly_rate: float

    @staticmethod
    def from_dict(data: dict) -> "Employee":

        rate_keys = ["hourly_rate", "rate", "salary"]

        rate_value = None
        for key in rate_keys:
            if key in data:
                rate_value = data[key]
                break
        if rate_value is None:
            raise ValueError("Отсутствует поле с почасовой ставкой (hourly_rate / rate / salary)")

        try:
            return Employee(
                id=int(data["id"]),
                email=data["email"].strip(),
                name=data["name"].strip(),
                department=data["department"].strip(),
                hours_worked=float(data["hours_worked"]),
                hourly_rate=float(rate_value)
            )
        except (KeyError, ValueError) as e:
            raise ValueError(f"Некорректные данные сотрудника: {e}")

    def payout(self) -> float:
        return self.hours_worked * self.hourly_rate
