from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import logging
import yaml


def main():
    logging.basicConfig(level=logging.INFO)

    with open("config/config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    try:
        logging.info("Starting ETL process...")

        # Extract
        raw_data = extract_data(config['extract'])
        logging.info("Data extraction complete.")

        # Transform
        transformed_data = transform_data(raw_data, config['transform'])
        logging.info("Data transformation complete.")

        # Load
        load_data(transformed_data, config['load'])
        logging.info("Data loading complete.")

    except Exception as e:
        logging.error(f"ETL process failed: {e}")


if __name__ == "__main__":
    main()
