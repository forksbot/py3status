# -*- coding: utf-8 -*-
'''
Ultimately customizable weather module based on the IP-API Geolocation API
(http://ip-api.com) and the OpenWeatherMap API (https://openweathermap.org).

Requires an API key for OpenWeatherMap (OWM), but the free tier allows you
enough requests/sec to get accurate weather even up to the second.

This module allows you to specify an icon for nearly every weather scenario
imaginable. The default configuration options lump many of the icons into
a few groups, and due to the limitations of UTF-8, this is really as expressive
as it gets.

I would highly suggest you install an additional font, such as the incredible
(and free!) Weather Icons font (https://erikflowers.github.io/weather-icons),
which has icons for most weather scenarios. But, this will still work with
the i3bar default font, Deja Vu Sans Mono font, which has Unicode support.
You can see the (limited) weather icon support within Unicode in the defaults.

For more information, see the documentation
(https://openweathermap.org/weather-conditions) on what weather conditions are
supported. See the configuration options for how to specify each weather icon.

Configuration parameters:
    api_key: Your OpenWeatherMap API key.
        See https://openweathermap.org/appid
        (default None)
    cache_timeout: The time between weather polling in seconds
        It is recommended to keep this at a higher value to avoid rate
        limiting with the API's.
        (default 600)
    color_neg_20: Color for a Fahrenheit temperature of -20°.
       Defaults to a magenta.
       (default '#FF00FF')
    color_neg_60: Color for a Fahrenheit temperature of -60°.
       Defaults to a deep purple.
       (default '#6B006B')
    color_pos_120: Color for a Fahrenheit temperature of 120°.
       Defaults to a white.
       (default '#FFFFFF')
    color_pos_30: Color for a Fahrenheit temperature of 30°.
       Defaults to a cyan.
       (default '#00FFFF')
    color_pos_40: Color for a Fahrenheit temperature of 40°.
       Defaults to a green.
       (default '#7FFF00')
    color_pos_50: Color for a Fahrenheit temperature of 50°.
       Defaults to a yellow.
       (default '#7FFF00')
    color_pos_70: Color for a Fahrenheit temperature of 70°.
       Defaults to a orange.
       (default '#FF9900')
    color_pos_90: Color for a Fahrenheit temperature of 90°.
       Defaults to a red.
       (default '#FF0000')
    color_zero: Color for a Fahrenheit temperature of zero.
        Defaults to a blue.
        (default '#0000FF')
    forecast_days: Number of days to include in the forecast, including today
        (regardless of the 'forecast_include_today' flag)
        (default 0)
    forecast_include_today: Include today in the forecast? (Boolean)
        (default False)
    forecast_text_separator: Separator between entries in the forecast
        (default ' ')
    format: How to display the weather. This also dictates the type of
        forecast. The placeholders here refer to the format_[...] variables
        found below.
        Available placeholders:
            icon, clouds, rain, snow, wind, humidity, pressure, temp, sunrise,
            sunset, desc, desc_long, forecast
        You may also use the icons in the icon dictionary with their identifiers
        (default '{icon}: {temp} {desc}')
    format_clouds: Formatting for cloud coverage (percentage).
        Available placeholders:
            icon, coverage
        (default '{icon}: {coverage}%')
    format_forecast: Formatting for future forecasts
        Available placeholders:
            See 'format'
        This is similar to the 'format' field, but contains information
        for future weather
        (default '{icon}')
    format_humidity: Formatting for humidity (percentage)
        Available placeholders:
            icon, humid
        (default '{icon}: {humid}%')
    format_pressure: Formatting for atmospheric pressure
        Available placeholders:
            icon, press, sea_level
        (default '{icon}: {press} hPa')
    format_rain: Formatting for rain volume over the past 3 hours
        Available placeholders:
            icon, amt
        (default '{icon}: {amt} inches')
    format_snow: Formatting for snow volume over the past 3 hours
        Available placeholders:
            icon, amt
        (default '{icon}: {amt} inches')
    format_sunrise: Formatting for sunrise time.
        Note that this format accepts strftime/strptime placeholders to populate
        the output with the time information.
        Available placeholders:
            icon
        (default '{icon}: %X')
    format_sunset: Formatting for sunset time.
        This format accepts strftime/strptime placeholders to populate the
        output with the time information.
        Available placeholders:
            icon
        (default '{icon}: %X')
    format_temp: Formatting for temperature
        Available placeholders:
            cur, icon, max, min
        (default '{icon}: {cur}°')
    format_wind: Formatting for wind degree and speed
        Available placeholders:
            icon, deg, speed, gust
        (default '{icon}: {speed} mph')
    icon_atmosphere: Icon for atmospheric conditions, like fog, smog, etc.
        (default '🌫')
    icon_breeze: Icon for wind or breeze
        (default '☴')
    icon_cloud: Icon for clouds
        (default '☁')
    icon_extreme: Icon for extreme weather
        (default '⚠')
    icon_humidity: Icon for humidity
        (default '●')
    icon_pressure: Icon for pressure
        (default '◌')
    icon_rain: Icon for rain
        (default '🌧')
    icon_snow: Icon for snow
        (default '❄')
    icon_sun: Icon for sunshine
        (default '☼')
    icon_temp: Icon for temperature
        (default '○')
    icon_thunderstorm: Icon for thunderstorms
        (default '⛈')
    icons: A dictionary relating weather code to icon.
        See https://openweathermap.org/weather-conditions for a complete list
        of supported icons. This will fall-back to the listed icon if there is
        no specific icon present.
        There are multiple ways to specify individual icons based on the id:
            - Use the key 'i601' to reference the condition with id = 601
              (snow)
            - Use the key 'i230_i232' to reference a span of conditions
              inclusive, in this case conditions (230, 231, 232) (thunderstorm
              with drizzle)
        Also, you can specify the icons for the various formatting sections
        below. For example, to specify the icon for 'format_pressure', use
        'pressure'. A few formatting sections will take from the defaults or be
        dynamic, including
            - clouds
            - rain
            - wind
            - sunrise
            - sunset
        These may be specified regardless.
        (default None)
    lang: An ISO 639-1 code for your language (two letters)
        (default 'en')
    rain_unit: Unit for rain fall
        Options:
            cm, ft, in, mm, m, yrd
        (default 'in')
    request_timeout: The timeout in seconds for contacting the IP API.
        (default 10)
    snow_unit: Unit for snow fall
        Options:
            cm, ft, in, mm, m, yrd
        (default 'in')
    temp_color: Color the temperature output based on a color scale.
        For reference, see https://goo.gl/NGbjIE
        (default False)
    temp_unit: Unit for temperature
        Options:
            c, f, k
        (default 'f')
    wind_unit: Unit for wind speed
        Options:
            fsec, msec, mph, kmh
        (default 'mph')

Format Placeholders:
    - All:
        - {icon}: The icon associated with a formatting section
    - format_cloud:
        - {coverage}: Cloud coverage percentage.
    - format_humidity:
        - {humid}: The humidity percentage
    - format_pressure:
        - {press}: The measurement of current atmospheric pressure in Pascals
        - {sea_level}: The measurement of current atmospheric pressure at
          sea-level in Pascals.
    - format_rain:
        - {amt}: Measurement of the amount of rain in the configured unit
    - format_snow:
        - {amt}: Measurement of the amount of snow in the configured unit
    - format_temp:
        - {max}: The maximum temperature in the configured unit.
        - {min}: The minimum temperature in the configured unit.
        - {cur}: Current temperature in the configured unit.
    - format_wind:
        - {deg}: Current wind speed heading (in degrees).
        - {gust}: The speed of current wind gusts in the configured unit.
        - {speed}: The speed of the wind in the configured unit.
    - format only:
        - {forecast}: Contains the formatted result of format_forecast.
    - format, format_forecast:
        - {clouds}: Contains the formatted result of format_clouds.
        - {desc_long}: Natural description of the current weather.
        - {desc}: Short description of the current weather.
        - {humidity}: Contains the formatted result of format_humidity.
        - {pressure}: Contains the formatted result of format_pressure.
        - {snow}: Contains the formatted result of format_snow.
        - {sunrise}: Contains the formatted result of format_sunrise.
        - {sunset}: Contains the formatted result of format_sunset.
        - {temp}: Contains the formatted result of format_temp.
        - {wind}: Contains the formatted result of format_wind.

Example configuration:
```
weather_owm {
  api_key = '...'

  icons {
    i200 = "☔"
    i230_i232 = "🌧"

    clouds = "☁"
  }

  format = '{icon}: {temp}, {forecast}'
  forecast_days = 3
}
```
Outputs: 🌫: ○: 59°, ⛅ ☼ 🌧`
- Currently foggy, 59° F outside, with forecast of cloudy tomorrow, sunny the
  next day, then rainy


@author alexoneill
@licence MIT
'''

import datetime


# API information
OWM_API = '2.5'
OWM_CURR_ENDPOINT = 'http://api.openweathermap.org/data/%s/weather?' \
    'APPID=%s&lat=%f&lon=%f&lang=%s'
OWM_FUTURE_ENDPOINT = 'http://api.openweathermap.org/data/%s/forecast?' \
    'APPID=%s&lat=%f&lon=%f&lang=%s&cnt=%%d'
IP_ENDPOINT = 'http://ip-api.com/json'

# Paths of information to extract from JSON
IP_LAT = '//lat'
IP_LNG = '//lon'
OWM_WEATHER_ICON = '//weather:0/id'
OWM_CLOUD_COVER = '//clouds/all'
OWM_RAIN = '//rain/3h'
OWM_SNOW = '//snow/3h'
OWM_WIND = '//wind'
OWM_HUMIDITY = '//main'
OWM_PRESSURE = '//main'
OWM_TEMP = '//main'
OWM_SUNRISE = '//sys/sunrise'
OWM_SUNSET = '//sys/sunset'
OWM_DESC = '//weather:0/main'
OWM_DESC_LONG = '//weather:0/description'

# Units constants
RAIN_UNITS = set(['cm', 'ft', 'in', 'mm', 'm', 'yrd'])
SNOW_UNITS = RAIN_UNITS
TEMP_UNITS = set(['c', 'f', 'k'])
WIND_UNITS = set(['fsec', 'msec', 'mph', 'kmh'])


class OWMException(Exception):
    pass


class Py3status:

    api_key = None
    cache_timeout = 600
    color_neg_20 = '#FF00FF'
    color_neg_60 = '#6B006B'
    color_pos_120 = '#FFFFFF'
    color_pos_30 = '#00FFFF'
    color_pos_40 = '#7FFF00'
    color_pos_50 = '#7FFF00'
    color_pos_70 = '#FF9900'
    color_pos_90 = '#FF0000'
    color_zero = '#0000FF'
    forecast_days = 0
    forecast_include_today = False
    forecast_text_separator = ' '
    format = '{icon}: {temp} {desc}'
    format_clouds = '{icon}: {coverage}%'
    format_forecast = '{icon}'
    format_humidity = '{icon}: {humid}%'
    format_pressure = '{icon}: {press} hPa'
    format_rain = '{icon}: {amt} inches'
    format_snow = '{icon}: {amt} inches'
    format_sunrise = '{icon}: %X'
    format_sunset = '{icon}: %X'
    format_temp = u'{icon}: {cur}°'
    format_wind = '{icon}: {speed} mph'
    icon_atmosphere = u'🌫'
    icon_breeze = u'☴'
    icon_cloud = u'☁'
    icon_extreme = u'⚠'
    icon_humidity = u'●'
    icon_pressure = u'◌'
    icon_rain = u'🌧'
    icon_snow = u'❄'
    icon_sun = u'☼'
    icon_temp = u'○'
    icon_thunderstorm = u'⛈'
    icons = None
    lang = 'en'
    rain_unit = 'in'
    request_timeout = 10
    snow_unit = 'in'
    temp_color = False
    temp_unit = 'f'
    wind_unit = 'mph'

    def _get_icons(self):
        if self.icons is None:
            self.icons = {}

        # Defaults for weather ranges
        defaults = {
            'i200_i299': self.icon_thunderstorm,
            'i300_i399': self.icon_rain,
            'i500_i599': self.icon_rain,
            'i600_i699': self.icon_snow,
            'i700_i799': self.icon_atmosphere,
            'i800': self.icon_sun,
            'i801_i809': self.icon_cloud,
            'i900_i909': self.icon_extreme,
            'i950_i959': self.icon_breeze,
            'i960_i999': self.icon_extreme,
        }

        # Default mappings for other icons
        others = {
            'clouds': 802,
            'rain': 501,
            'snow': 601,
            'wind': 954,
            'humidity': self.icon_humidity,
            'pressure': self.icon_pressure,
            'temp': self.icon_temp,
            'sunrise': 800,
            'sunset': 801,
        }

        # Handling ranges from OpenWeatherMap
        data = {}
        for source in (defaults, self.icons):
            for key in source:
                if (key[0] != 'i' and key not in others):
                    raise Exception('Icon identifier is invalid! (%s)' % key)

                if key[0] == 'i':
                    if '_' in key:
                        if key.count('_i') != 1:
                            raise Exception('Icon range is not properly'
                                            'formatted! (%s)' % key)

                        # Populate each code
                        (start, end) = tuple(map(int, key[1:].split('_i')))
                        for code in range(start, end + 1):
                            data[code] = source[key]

                    else:
                        data[int(key[1:])] = source[key]
                else:
                    data[key] = source[key]

        # Weather icons for formatting sections
        for key in others:
            if key not in data:
                if isinstance(others[key], int):
                    data[key] = data[others[key]]
                else:
                    data[key] = others[key]

        return data

    def post_config_hook(self):
        # Verify the API key
        if self.api_key is None:
            raise OWMException('API Key for OpenWeatherMap cannot be empty!'
                               ' Go to http://openweathermap.org/appid to'
                               ' get an API Key.')

        # Generate our icon array
        self.icons = self._get_icons()

        # Conversion factors
        self.in_from_mm = 0.0393701
        self.ft_from_meter = 3.28084
        self.kmh_from_msec = 0.277778
        self.mph_from_msec = 2.23694

        # Verify the units configuration
        if self.rain_unit not in RAIN_UNITS:
            raise Exception('rain_unit is not recognized')

        if self.snow_unit not in SNOW_UNITS:
            raise Exception('snow_unit is not recognized')

        if self.temp_unit not in TEMP_UNITS:
            raise Exception('temp_unit is not recognized')

        if self.wind_unit not in WIND_UNITS:
            raise Exception('wind_unit is not recognized')

    def _get_coords(self):
        # Contact the IP API
        try:
            req = self.py3.request(IP_ENDPOINT,
                                   timeout=self.request_timeout)
            data = req.json()
        except (self.py3.RequestException):
            return None
        except (self.py3.RequestURLError):
            return None

        # Extract the data
        return (self._jpath(data, IP_LAT, 0), self._jpath(data, IP_LNG, 0))

    def _get_req_url(self, base, coords):
        # Construct the url from the pattern
        params = [OWM_API, self.api_key] + list(coords) + [self.lang]
        return base % tuple(params)

    def _make_req(self, url):
        # Make a request expecting a JSON response
        req = self.py3.request(url, timeout=self.request_timeout)
        if req.status_code != 200:
            data = req.json()
            raise OWMException(data['message'])

        return req.json()

    def _jpath(self, data, query, default=None):
        # Take the query expression and drill down into the given dictionary
        parts = query.strip('/').split('/')
        for part in parts:
            try:
                # This represents a key:index expression, representing first
                # selecting a key, then an index
                if ':' in part:
                    (part, index) = tuple(part.split(':'))
                    data = data[part]
                    data = data[int(index)]

                # Select a portion of the dictionary by key in the path
                else:
                    data = data[part]

            # Failed, so return the default
            except (KeyError, IndexError, TypeError):
                return default

        return data

    def _get_weather(self, coords):
        # Get and process the current weather
        url = self._get_req_url(OWM_CURR_ENDPOINT, coords)
        return self._make_req(url)

    def _get_forecast(self, coords):
        # Get the next few days
        if self.forecast_days == 0:
            return []

        # Get raw data
        url = (self._get_req_url(OWM_FUTURE_ENDPOINT, coords)
               % (self.forecast_days + 1))
        data = self._make_req(url)

        # Extract forecast
        weathers = data['list']
        return weathers[:-1] if (self.forecast_include_today) else weathers[1:]

    def _color_gradient(self, start, end):
        # Convert a hexadecimal string to RGB tuple
        def hexToRGB(hexstr):
            # Get strings
            hexstr = hexstr.lstrip('#')
            (r, g, b) = (hexstr[:2], hexstr[2:4], hexstr[4:6])

            # Give numbers
            def convert(x):
                return int(x, base=16)

            return (convert(r), convert(g), convert(b))

        def rgbToHex(rgb):
            # Convert a collection of RGB values into a hexadecimal string
            chars = map(lambda x: '%02x' % int(x), list(rgb))
            return ''.join(chars)

        def calc(val):
            # Get the RGB of start and finish
            (r1, g1, b1) = hexToRGB(start)
            (r2, g2, b2) = hexToRGB(end)

            # Blend from one to the next for each R, G, B
            # Assume the input here is a number [0, 1.0] inclusive
            def line(a, b, x):
                return a + x * float(b - a)

            new = (line(r1, r2, val), line(g1, g2, val), line(b1, b2, val))

            # Convert back to what we got
            return rgbToHex(new)

        # We return a function
        return calc

    def _get_icon(self, wthr):
        # Lookup the icon from the weather code (default sunny)
        return self.icons[self._jpath(wthr, OWM_WEATHER_ICON, 800)]

    def _format_clouds(self, wthr):
        # Format the cloud cover (default clear)
        return self.py3.safe_format(self.format_clouds, {
            'icon': self.icons['clouds'],
            'coverage': self._jpath(wthr, OWM_CLOUD_COVER, 0),
        })

    def _format_rain(self, wthr):
        # Format rain fall
        rain = self._jpath(wthr, OWM_RAIN, 0)

        # Data comes as mm
        inches = rain * self.in_from_mm

        options = {
            'icon': self.icons['rain'],
            'mm': round(rain),
            'cm': round(rain / 10),
            'm': round(rain / 100),
            'in': round(inches),
            'ft': round(inches / 12),
            'yrd': round(inches / 36)}

        # Format the rain fall
        return self.py3.safe_format(self.format_rain, {
            'amt': options[self.rain_unit],
        })

    def _format_snow(self, wthr):
        # Format snow fall
        snow = self._jpath(wthr, OWM_SNOW, 0)

        # Data comes as mm
        inches = snow * self.in_from_mm

        options = {
            'icon': self.icons['snow'],
            'mm': round(snow),
            'cm': round(snow / 10),
            'm': round(snow / 100),
            'in': round(inches),
            'ft': round(inches / 12),
            'yrd': round(inches / 36)}

        # Format the snow fall
        return self.py3.safe_format(self.format_snow, {
            'amt': options[self.snow_unit],
        })

    def _format_wind(self, wthr):
        wind = self._jpath(wthr, OWM_WIND, dict())

        # Speed and Gust
        msec_speed = wind['speed'] if ('speed' in wind) else 0
        msec_gust = wind['gust'] if ('gust' in wind) else 0

        options = {
            'fsec': {
                'speed': msec_speed * self.ft_from_meter,
                'gust': msec_gust * self.ft_from_meter},
            'msec': {
                'speed': msec_speed,
                'gust': msec_gust},
            'mph': {
                'speed': msec_speed * self.mph_from_msec,
                'gust': msec_gust * self.mph_from_msec},
            'kmh': {
                'speed': msec_speed * self.kmh_from_msec,
                'gust': msec_gust * self.kmh_from_msec}}

        # Get the choice and add more
        choice = options[self.wind_unit]
        choice['icon'] = self.icons['wind']
        choice['deg'] = wind['deg'] if ('deg' in wind) else 0

        # Format the wind speed
        return self.py3.safe_format(self.format_wind, choice)

    def _format_humidity(self, wthr):
        # Format the humidity (default zero humidity)
        return self.py3.safe_format(self.format_humidity, {
            'icon': self.icons['humidity'],
            'humid': self._jpath(wthr, OWM_HUMIDITY, 0),
        })

    def _format_pressure(self, wthr):
        # Get data and add the icon
        pressure = self._jpath(wthr, OWM_PRESSURE, dict())
        pressure['icon'] = self.icons['pressure']

        # Format the barometric pressure
        return self.py3.safe_format(self.format_humidity, pressure)

    def _format_temp(self, wthr):
        # Get Kelvin data (default absolute zero)
        kelvin = self._jpath(wthr, OWM_TEMP, 0)

        # Temperature conversion methods
        def kToC(val):
            return val - 273.15

        def kToF(val):
            return val * (9.0 / 5.0) - 459.67

        # Determine color based on temperature
        # Gradients below have a lower limit, upper limit, and
        # a transition function
        options = [
            (None, -60, lambda _: self.color_neg_60),
            (-60, -20, self._color_gradient(self.color_neg_60,
                                            self.color_neg_20)),
            (-20, 0, self._color_gradient(self.color_neg_20,
                                          self.color_zero)),
            (0, 30, self._color_gradient(self.color_zero,
                                         self.color_pos_30)),
            (30, 40, self._color_gradient(self.color_pos_30,
                                          self.color_pos_40)),
            (40, 50, self._color_gradient(self.color_pos_40,
                                          self.color_pos_50)),
            (50, 70, self._color_gradient(self.color_pos_50,
                                          self.color_pos_70)),
            (70, 90, self._color_gradient(self.color_pos_70,
                                          self.color_pos_90)),
            (90, 120, self._color_gradient(self.color_pos_90,
                                           self.color_pos_120)),
            (120, None, lambda _: self.color_pos_120)]

        color = None
        if self.temp_color:
            temp = kToF(kelvin['temp'])

            # Go trough options
            for (lower, upper, fn) in options:
                # Adjust boundaries
                lower = temp - 1 if(lower is None) else lower
                upper = temp + 1 if(upper is None) else upper

                # This should happen at least once
                if lower < temp <= upper:
                    color = fn((temp - lower) / float(upper - lower))
                    break

        # Optionally add the color
        format_str = self.format_temp
        if self.temp_color:
            color_str = '\?color=%s' % color
            format_str = color_str + ' ' + format_str

        options = {
            'c': {
                'cur': round(kToC(kelvin['temp'])),
                'max': round(kToC(kelvin['temp_max'])),
                'min': round(kToC(kelvin['temp_min']))},
            'f': {
                'cur': round(kToF(kelvin['temp'])),
                'max': round(kToF(kelvin['temp_max'])),
                'min': round(kToF(kelvin['temp_min']))},
            'k': {
                'cur': round(kelvin['temp']),
                'max': round(kelvin['temp_max']),
                'min': round(kelvin['temp_min'])}}

        # Get the choice and add more
        choice = options[self.temp_unit]
        choice['icon'] = self.icons['temp']

        # Format the temperature
        return self.py3.safe_format(self.format_temp, choice)

    def _format_sunrise(self, wthr):
        # Get the time for sunrise (default is the start of time)
        dt = datetime.datetime.utcfromtimestamp(
            self._jpath(wthr, OWM_SUNRISE, 0))

        # Format the sunrise
        replaced = dt.strftime(self.format_sunrise)
        return self.py3.safe_format(replaced, {
            'icon': self.icons['sunrise'],
        })

    def _format_sunset(self, wthr):
        # Get the time for sunset (default is the start of time)
        dt = datetime.datetime.utcfromtimestamp(
            self._jpath(wthr, OWM_SUNSET, 0))

        # Format the sunset
        replaced = dt.strftime(self.format_sunset)
        return self.py3.safe_format(replaced, {
            'icon': self.icons['sunset'],
        })

    def _format_dict(self, wthr):
        return {
            # Standard options
            'icon': self._get_icon(wthr),
            'clouds': self._format_clouds(wthr),
            'rain': self._format_rain(wthr),
            'snow': self._format_rain(wthr),
            'wind': self._format_wind(wthr),
            'humidity': self._format_humidity(wthr),
            'pressure': self._format_pressure(wthr),
            'temp': self._format_temp(wthr),
            'sunrise': self._format_sunrise(wthr),
            'sunset': self._format_sunset(wthr),

            # Descriptions (defaults to empty)
            'desc': self._jpath(wthr, OWM_DESC, '').lower(),
            'desc_long': self._jpath(wthr, OWM_DESC_LONG, '')
        }

    def _format(self, wthr, fcsts):
        # Format all sections
        today = self._format_dict(wthr)

        # Insert forecasts
        forecasts = []
        for day in fcsts:
            future = self._format_dict(day)
            forecasts.append(self.py3.safe_format(self.format_forecast, future))

        # Give the final format
        today['forecast'] = self.py3.composite_join(
            self.forecast_text_separator, forecasts)
        return self.py3.safe_format(self.format, today)

    def weather(self):
        # Get weather information
        coords = self._get_coords()
        text = ''
        if coords is not None:
            wthr = self._get_weather(coords)
            fcsts = self._get_forecast(coords)

            text = self._format(wthr, fcsts)

        return {
            'full_text': text,
            'cached_until': self.py3.time_in(seconds=self.cache_timeout)
        }

    def on_click(self, event):
        # Avoid hitting rate limits on APIs
        self.py3.prevent_refresh()


if __name__ == '__main__':
    '''
    Run module in test mode.
    '''

    import os
    from py3status.module_test import module_test
    module_test(Py3status, config={
        'api_key': os.getenv('OWM_API_KEY'),

        'icons': {
            'i200': "☔",
            'i230_i232': "🌧",

            'clouds': "☁",
        },

        'format': '{icon}: {temp} {desc}, {forecast}',
        'forecast_days': 3,
        'temp_color': True,
    })
