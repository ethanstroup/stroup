from vetiver import VetiverModel
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins

load_dotenv(find_dotenv())

b = pins.board_folder('/data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240413T223313Z-19257')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app

vetiver_api.run(port = 8080)
