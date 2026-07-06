

class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    
    def to_html(self):
        raise NotImplemented
    

    def props_to_html(self):
        props_str = ""
        if self.props:
            for key, value in self.props.items():
                props_str += f''' {key}="{value}"'''
            return props_str


        return None
    




    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"