from commons.cores.base_model import BaseModel, MixinFields, MixinFunctions


class DemoOrm(BaseModel, MixinFields, MixinFunctions):
    __tablename__ = "demos"
    __table_args__ = {"comment": "演示表"}
