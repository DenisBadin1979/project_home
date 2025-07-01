from src.masks import det_masks_card_number, get_masks_account
from src.utils import operations_json

if __name__ == "__main__":
    print(operations_json("data/operations.json"))
    print(det_masks_card_number("1234567891012456"))

    print(get_masks_account("73654108430131574305"))
