
class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None):
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
    

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        temp_str = ""
        if not self.value and self.value != "":
            raise ValueError("All leaf nodes must have a value")
        elif not self.tag:
            return self.value
        elif self.tag == "a":
            key, value = next(iter(self.props.items()))
            return f'''<{self.tag} {key}="{value}">{self.value}</{self.tag}>'''
        elif self.tag == "img":
            for key, value in self.props.items():
                temp_str += f''' {key}="{value}"'''
            return f"<{self.tag}{temp_str}>"
        else:
            return f'''<{self.tag}>{self.value}</{self.tag}>'''

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Props: {self.props}"
    

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        html_str = ""
        if not self.tag:
            raise ValueError("Parent nodes require tag attribute")
        elif not self.children:
            raise ValueError("Parent nodes require children attribute")
        else:
            for item in self.children:
                temp = item.to_html()
                html_str += temp
        return f'<{self.tag}>{html_str}</{self.tag}>'
    
    def __repr__(self):
        return f"Tag: {self.tag}, Children: {self.children}, Props: {self.props}"