from .models import Property_Residential, Property_Commercial, Property_Plot, Property_PG, Property_Images

def add_variable_to_context(request):
    return {
        'bedroom_choices': {

            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
        },

        'bathroom_choices': {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
        },

        'balcony_choices': {

            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,

        },

        'price_choices': {

            '200000': '200,000',
            '300000': '300,000',
            '400000': '400,000',
            '500000': '500,000',
            '1000000': '10,00,000',
            '1500000': '25,00,000',
            '2000000': '20,00,000',
            '2500000': '25,00,000',
            '4000000': '40,00,000',
            '5000000': '50,00,000',

        },

        'state_choices': {

            "AN": "Andaman and Nicobar Islands",
            "AP": "Andhra Pradesh",
            "AR": "Arunachal Pradesh",
            "AS": "Assam",
            "BR": "Bihar",
            "CG": "Chandigarh",
            "CH": "Chhattisgarh",
            "DN": "Dadra and Nagar Haveli",
            "DD": "Daman and Diu",
            "DL": "Delhi",
            "GA": "Goa",
            "GJ": "Gujarat",
            "HR": "Haryana",
            "HP": "Himachal Pradesh",
            "JK": "Jammu and Kashmir",
            "JH": "Jharkhand",
            "KA": "Karnataka",
            "KL": "Kerala",
            "LA": "Ladakh",
            "LD": "Lakshadweep",
            "MP": "Madhya Pradesh",
            "MH": "Maharashtra",
            "MN": "Manipur",
            "ML": "Meghalaya",
            "MZ": "Mizoram",
            "NL": "Nagaland",
            "OR": "Odisha",
            "PY": "Puducherry",
            "PB": "Punjab",
            "RJ": "Rajasthan",
            "SK": "Sikkim",
            "TN": "Tamil Nadu",
            "TS": "Telangana",
            "TR": "Tripura",
            "UP": "Uttar Pradesh",
            "UK": "Uttarakhand",
            "WB": "West Bengal"

        }

    }


