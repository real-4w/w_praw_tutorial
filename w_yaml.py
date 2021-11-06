import yaml
def ProcessYAML (yaml_file) :
    """This function opens the yaml file and returns the data objec

    Args:
        yaml_file (file): yaml file to be loaded

    Returns:
        (boolean, object): returns debug flag and the yaml object
    """
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (debug, y_data)  
