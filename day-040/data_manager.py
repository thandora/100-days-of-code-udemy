import os
from dotenv import load_dotenv
import requests

"""Class for talking with Sheety API"""

load_dotenv(".env")
prices_sheet_epoint = os.getenv("PRICES_EPOINT")
users_sheet_epoint = os.getenv("USERS_EPOINT")


class DataManager:
    """Responsible for getting and updating data of destination, and
    users sheet stored in google sheets. Uses Sheety API
    """

    def __init__(self) -> None:
        self.sheet_endpoint = prices_sheet_epoint
        self.destination_data = None
        self.users = self.get_users()

    def get_destination_data(self) -> dict:
        """Get sheet data from google sheets

        Returns:
            dict: sheet data
        """

        r = requests.get(url=self.sheet_endpoint)
        self.destination_data = r.json()["prices"]
        return self.destination_data

    def update_price(self, id, new_price: int) -> None:
        """Update entry in sheet referenced by <id> with the updated
        lowest price <new_price>.

        Args:
            id (str): _description_
            new_price (_type_): _description_
        """

        url = f"{prices_sheet_epoint}/{id}"
        updated_data = {
            "price": {
                "lowestPrice": new_price,
            }
        }

        requests.put(url=url, json=updated_data)

    def register_user(self) -> None:
        """Prompts user to register, update sheet with new user, and add
        user to class' users list.
        """

        # Ask new member's details
        first_name = input("First name: ")
        last_name = input("Last name: ")

        user_email = input("Email: ")
        confirm_email = input("Email: ")

        while user_email != confirm_email:
            print("Emails do not match. Enter email again")
            user_email = input("Email: ")
            confirm_email = input("Email: ")

        user_details = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": user_email,
            }
        }

        # Update data sheet
        r = requests.post(url=users_sheet_epoint, json=user_details)

        # Add user to class' users list
        self.users.append(r.json()["user"])
        print("Registration complete. Welcome to the club ")

    def get_users(self) -> None:
        """Get users info from sheet."""

        r = requests.get(url=users_sheet_epoint)
        return r.json()["users"]

    def get_emails(self) -> list:
        """Create a list of user emails from self.users.

        Returns:
            list: user emails
        """

        emails = [user["email"] for user in self.users]
        return emails
