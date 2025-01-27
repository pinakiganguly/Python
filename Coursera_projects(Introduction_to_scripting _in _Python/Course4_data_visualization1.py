"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    dic = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for line in csvreader:
            key = line[keyfield]
            dic[key] = line
    return dic

def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    converter_dict = {}
    filename = codeinfo['codefile']
    separator = codeinfo['separator']
    quote = codeinfo['quote']
    keyfield = codeinfo['plot_codes']
    data_code = codeinfo['data_codes']
    code_file = read_csv_as_nested_dict(filename, keyfield, separator, quote)
    for key in code_file:
        converter_dict[key] = code_file[key][data_code]
    return converter_dict


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    counter = 0
    converter = build_country_code_converter(codeinfo)
    code_dict = {}
    reconcile_dict = {}
    out_set = set()
    plot_key = plot_countries.keys()
    gdp_key = gdp_countries.keys()
    for key in plot_key:
        for keys in converter:
            if key.lower() == keys.lower():
                code_dict[key] = converter[keys]
                counter += 1
            else:
                continue
        if counter == 0:
            code_dict[key] = ''
        counter = 0
    for item in code_dict:
        for items in gdp_key:
            if code_dict[item].lower() == items.lower():
                reconcile_dict[item] = items
                counter += 1
            else:
                continue
        if counter == 0:
            out_set.add(item)
        counter = 0
    return (reconcile_dict, out_set)

def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    filename = gdpinfo['gdpfile']
    keyfield = gdpinfo['country_code']
    separator = gdpinfo['separator']
    quote = gdpinfo['quote']
    year_set = set()
    gdp_data = read_csv_as_nested_dict(filename, keyfield, separator, quote)
    country_code = reconcile_countries_by_code(codeinfo, plot_countries, gdp_data)
    gdp_dict = country_code[0]
    gdp_value = {}
    for key in gdp_dict:
        if year in gdp_data[gdp_dict[key]]:
            gdp = gdp_data[gdp_dict[key]][year]
            if gdp != "":
                gdp_value[key] = math.log(float(gdp), 10)
            else:
                year_set.add(key)
        else:
            continue
    return (gdp_value, country_code[1], year_set)

def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    worldmap_chart = pygal.maps.world.World()
    gdpmapdict = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)
    worldmap_chart.title = "Gross domestic products for " + year + " (source: World Bank)"
    worldmap_chart.add(year, gdpmapdict[0])
    worldmap_chart.render_to_file(map_file)
    worldmap_chart.render_in_browser()

def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

#test_render_world_map()
