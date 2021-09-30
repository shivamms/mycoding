class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
    
        def getWordsWithPrefix(products, prefix):
            productList = []
            length = len(prefix)
            for product in products:
                if product[:length] == prefix:
                    productList.append(product)
            productList = sorted(productList)[:3]

            return productList[:3] if len(productList) > 3 else productList

        prefix = ''
        for letter in searchWord:
            prefix += letter
            result.append(getWordsWithPrefix(products, prefix))
        return result