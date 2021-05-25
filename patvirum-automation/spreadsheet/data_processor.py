from uuid import uuid1

from spreadsheet.sheets import Sheets
from settings import SCOPES, CREDENTIALS, TOKEN_PICKLE, SPREADSHEET_ID


class DataProcessor(Sheets):

    def __init__(self, spreadsheet_id, credentials=CREDENTIALS, token_pickle=TOKEN_PICKLE):
        super().__init__(spreadsheet_id, credentials, token_pickle)
        self.products_data = None

        self.products = self.get_sheet_values("Products").get('values', [])
        self.attributes = self.get_sheet_values("Attributes").get('values', [])
        self.variants = self.get_sheet_values("Variants").get('values', [])
        self.variant_attributes = self.get_sheet_values("Variant Attributes").get('values', [])

    def process_data(self):
        self.products_data = [
            {
                'id': self._safe_get(product, 0),
                'type': self._safe_get(product, 1),
                'title': self._safe_get(product, 2),
                'description': self._safe_get(product, 3),
                'price': self._safe_get(product, 4),
                'company': self._safe_get(product, 5),
                'category': self._safe_get(product, 6),
                'collection': self._safe_get(product, 7),
                'atributes': [
                    {
                        'product_id': self._safe_get(attribute, 0),
                        'name': self._safe_get(attribute, 1),
                        'value': self._safe_get(attribute, 2)
                    } for attribute in self.get_attributes_by_id(self._safe_get(product, 0))
                ],
                'variants': [
                    {
                        'product_id': self._safe_get(variant, 1),
                        'sku': self._safe_get(variant, 2) or f'n-{uuid1().time_low}',
                        'price': self._safe_get(variant, 3),
                        'atributes': [
                            {
                                'variant_id': self._safe_get(attribute, 0),
                                'name': self._safe_get(attribute, 1),
                                'value': self._safe_get(attribute, 2)
                            } for attribute in self.get_variant_attributes_by_id(self._safe_get(variant, 0))
                        ],
                    } for variant in self.get_variants_by_id(self._safe_get(product, 0))
                ]
            } for product in self.products[1:]
        ]

    def get_attributes_by_id(self, product_id):
        return filter(lambda items: items[0] == product_id, self.attributes[1:])

    def get_variants_by_id(self, product_id):
        return filter(lambda items: items[0] == product_id, self.variants[1:])

    def get_variant_attributes_by_id(self, variant_id):
        return filter(lambda items: items[0] == variant_id, self.variant_attributes[1:])

    @staticmethod
    def _safe_get(data, index):
        try:
            return data[index]
        except IndexError:
            return ''


if __name__ == '__main__':
    CREDENTIALS = 'credentials.json'
    TOKEN_PICKLE = 'token.pickle'
    data_processor = DataProcessor(SPREADSHEET_ID, CREDENTIALS, TOKEN_PICKLE)
    data_processor.process_data()
    import json

    print(json.dumps(data_processor.products_data, sort_keys=True, indent=4, ensure_ascii=False))
