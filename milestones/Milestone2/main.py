"""
The code below is just representative of the implementation of a Bot. 
However, this code was not meant to be compiled as it. It is the responsability 
of all the students to modifify this code such that it can fit the 
requirements for this assignments.
"""

import discord
import  os 
from discord.ext import commands
from models import *

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.command(name="test", description="write your database business requirement for this command here")
async def _test(ctx, arg1):
    testModel = TestModel(ctx, arg1)
    response = testModel.response()
    await ctx.send(response)


# TODO: complete the following tasks:
#       (1) Replace the commands' names with your own commands
#       (2) Write the description of your business requirement in the description parameter
#       (3) Implement your commands' methods.
# @bot.command(name="avgWeather", description="Get average temperature and humidity for a specific city")
# async def avgWeather(ctx, city_name: str):
#     try:
#         weather_report = CityModel.get_avg_weather_by_city()
#         city_weather = next((city for city in weather_report if city['city_name'].lower() == city_name.lower()), None)

#         if not city_weather:
#             await ctx.send(f"No weather data available for {city_name}.")
#             return

#         response = f"{city_weather['city_name']}: Avg Temp: {city_weather['avg_temp']}, Avg Humidity: {city_weather['avg_humidity']}"
#         await ctx.send(response)
#     except Exception as e:
#         await ctx.send(f"An error occurred: {e}")
@bot.command(name="recentNotifications", description="Displays the most recent notification")
async def recentNotification(ctx):
    try:
        recent_notification = NotificationModel().get_most_recent_notification()
        if not recent_notification:
            await ctx.send("No recent notifications.")
            return

        # Check if recent_notification is a dictionary and has the expected keys
        if isinstance(recent_notification, dict) and 'type' in recent_notification and 'count' in recent_notification:
            response = f"Type: {recent_notification['type']}, Count: {recent_notification['count']}"
        else:
            response = "Unexpected data format for notification."

        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(name="findFuelStations", description="Retrieves all fueling stations within the provided zipcode")
async def findFuelStations(ctx, zipcode: str):
    try:
        stations = FuelingStationModel().find_by_zipcode(zipcode)
        if not stations:
            await ctx.send(f"No fueling stations found for zipcode {zipcode}.")
            return

        # response = "\n".join([f"Station Name: ["test"], Location: {station['station_location']}" for station in stations])
        response = "test"
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")









@bot.command(name="cmd_2", description="database business requirement #2 here")
async def _command2(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_3", description="database business requirement #3 here")
async def _command3(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_4", description="database business requirement #4 here")
async def _command4(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_5", description="database business requirement #5 here")
async def _command5(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_6", description="database business requirement #6 here")
async def _command6(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_7", description="database business requirement #7 here")
async def _command7(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_8", description="database business requirement #8 here")
async def _command8(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_9", description="database business requirement #9 here")
async def _command9(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_10", description="database business requirement #10 here")
async def _command10(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_11", description="database business requirement #11 here")
async def _command11(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_12", description="database business requirement #12 here")
async def _command12(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_13", description="database business requirement #13 here")
async def _command13(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_14", description="database business requirement #14 here")
async def _command14(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_15", description="database business requirement #15 here")
async def _command15(ctx, *args):
    await ctx.send("This method is not implemented yet")


bot.run(TOKEN)
