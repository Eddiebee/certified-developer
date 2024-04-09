# maintenance test business logic

def test_maintenance(temperature:int, pressure:int):
    """_summary_

    Parameters
    ----------
    temperature : int
        test parameter for temperature sensor readings
    pressure : int
        parameter for hydraulic pressure 

    Returns
    -------
    str
        'Approved' or 'Denied' based on temperature or hydraulic pressure readings
    """
    maintenance_status = 'Needs Maintenance' if (temperature and temperature > 50) or (pressure and pressure > 2000) else 'No Maintenance Required'
    
    return maintenance_status