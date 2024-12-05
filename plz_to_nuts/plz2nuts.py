import argparse
from plz_to_nuts.main import get_median_region_by_prefix, get_nuts_by_name

def plz2nuts_cli():
    """
    Command-line interface to convert German postal codes to NUTS IDs.
    """
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Convert German postal code to NUTS ID.')
    parser.add_argument('postal_code', type=str, help='Postal code or prefix to lookup NUTS ID')

    # Parse the arguments
    args = parser.parse_args()

    # Get the postal code from the arguments
    postal_code = args.postal_code

    # Get the region dictionary using the postal code
    region = get_median_region_by_prefix(postal_code)

    if not region:
        print("No region found for the given postal code.")
        return

    # Get the NUTS ID using the region dictionary
    nuts_id = get_nuts_by_name(region)

    if nuts_id == "Not Found":
        print("No NUTS ID found for the given postal code.")
    else:
        print(nuts_id)


if __name__ == "__main__":
    plz2nuts_cli()
