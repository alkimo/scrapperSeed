import modules.parser
import modules.parser_treatment
import modules.driver_config
import modules.data_generator
import constant
import os

def main():
    cli_input = modules.parser.initParse()
    cli_input.n = modules.parser_treatment.treat_cli_name(cli_input.n)
    driver = modules.driver_config.select_driver(cli_input.b, constant.SCRIPT_PATH)
    scrapped_data_path = constant.SCRIPT_PATH + 'scrapped_data/' + cli_input.n
    os.mkdir(scrapped_data_path)
    driver.get(cli_input.url)
    modules.data_generator.generate_data(driver, scrapped_data_path)

    
if __name__ == "__main__":
    main()