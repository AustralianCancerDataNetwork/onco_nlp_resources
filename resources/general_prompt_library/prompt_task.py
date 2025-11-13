from pydantic import BaseModel, TypeAdapter
from typing import Dict

class PromptTask(BaseModel):
    question: str
    some_examples: Dict[str, BaseModel]

    def __init__(self, question: str, target_model: BaseModel, some_examples: Dict[str, Dict[str, str]]):
        super().__init__(question=question, some_examples={input: TypeAdapter(target_model).validate_python(ex) for input, ex in some_examples.items()})

    def get_prompt(self):
        q = self.question.strip()
        e = '\n\t'.join([f'{input}: {ex.model_dump_json()}' for input, ex in self.some_examples.items()])
        full_question = f'{q}\nHere are some examples, and the intended final answer for each example. \n\t{e}'
        return full_question

