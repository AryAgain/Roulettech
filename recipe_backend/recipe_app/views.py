from rest_framework.views import APIView
from rest_framework.response import Response
import random

class RandomDishView(APIView):
    def get(self, request):
        dishes = [
            'Spaghetti Carbonara', 'Chicken Curry', 'Grilled Cheese', 
            'Salmon Teriyaki', 'Tacos', 'Margherita Pizza', 
            'Beef Stroganoff', 'Vegetable Stir Fry', 'Chicken Alfredo', 
            'Pad Thai', 'Fish and Chips', 'Ratatouille', 
            'Pancakes', 'BBQ Ribs', 'Falafel Wrap', 
            'Miso Soup', 'Lasagna', 'Chili Con Carne', 
            'Eggplant Parmesan', 'Beef Tacos', 'Sushi Rolls', 
            'Fettuccine Alfredo', 'Chicken Biryani', 'Shakshuka', 
            'Pesto Pasta', 'Chicken Caesar Salad', 'Vegetable Curry', 
            'French Toast', 'Lamb Kebab', 'Butternut Squash Soup', 
            'Mushroom Risotto', 'Tom Yum Soup', 'Beef Wellington', 
            'Ramen', 'Pho', 'Gnocchi', 'Greek Salad', 
            'Pulled Pork Sandwich', 'Chicken Enchiladas', 'Seafood Paella', 
            'Stuffed Bell Peppers', 'Butter Chicken', 'Clam Chowder', 
            'Shepherd’s Pie', 'Avocado Toast', 'Chicken Satay', 
            'Beef Burgers', 'Spinach and Feta Pie', 'Peking Duck', 
            'Shrimp Scampi', 'Pumpkin Pie'
        ]
        selected_dish = random.choice(dishes)
        return Response({'dish': selected_dish})

class CookingTimerView(APIView):
    def post(self, request):
        dish = request.data.get('dish')
        dishes = {
                'Spaghetti Carbonara': 20 * 60,
                'Chicken Curry': 45 * 60,
                'Grilled Cheese': 10 * 60,
                'Salmon Teriyaki': 25 * 60,
                'Tacos': 15 * 60,
                'Margherita Pizza': 15 * 60,
                'Beef Stroganoff': 40 * 60,
                'Vegetable Stir Fry': 20 * 60,
                'Chicken Alfredo': 25 * 60,
                'Pad Thai': 30 * 60,
                'Fish and Chips': 35 * 60,
                'Ratatouille': 50 * 60,
                'Pancakes': 15 * 60,
                'BBQ Ribs': 120 * 60,
                'Falafel Wrap': 25 * 60,
                'Miso Soup': 15 * 60,
                'Lasagna': 90 * 60,
                'Chili Con Carne': 60 * 60,
                'Eggplant Parmesan': 45 * 60,
                'Beef Tacos': 20 * 60,
                'Sushi Rolls': 50 * 60,
                'Fettuccine Alfredo': 25 * 60,
                'Chicken Biryani': 60 * 60,
                'Shakshuka': 20 * 60,
                'Pesto Pasta': 20 * 60,
                'Chicken Caesar Salad': 15 * 60,
                'Vegetable Curry': 30 * 60,
                'French Toast': 10 * 60,
                'Lamb Kebab': 35 * 60,
                'Butternut Squash Soup': 40 * 60,
                'Mushroom Risotto': 45 * 60,
                'Tom Yum Soup': 30 * 60,
                'Beef Wellington': 120 * 60,
                'Ramen': 60 * 60,
                'Pho': 90 * 60,
                'Gnocchi': 30 * 60,
                'Greek Salad': 15 * 60,
                'Pulled Pork Sandwich': 90 * 60,
                'Chicken Enchiladas': 40 * 60,
                'Seafood Paella': 50 * 60,
                'Stuffed Bell Peppers': 45 * 60,
                'Butter Chicken': 50 * 60,
                'Clam Chowder': 45 * 60,
                'Shepherd’s Pie': 60 * 60,
                'Avocado Toast': 10 * 60,
                'Chicken Satay': 30 * 60,
                'Beef Burgers': 20 * 60,
                'Spinach and Feta Pie': 50 * 60,
                'Peking Duck': 120 * 60,
                'Shrimp Scampi': 25 * 60,
                'Pumpkin Pie': 60 * 60,
            }
        cooking_time = dishes.get(dish, 30 * 60)  # Default to 30 minutes if dish not found
        return Response({'cooking_time': cooking_time})
