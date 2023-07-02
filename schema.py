from marshmallow import Schema, fields, ValidationError, validates

class RaportSchema(Schema):
    year = fields.Int(required=True)
    month = fields.Int(required=True)
    out_days = fields.List(fields.Date(format='%d-%m-%Y'), required=True)
    output_file_path = fields.Str(required=True)
    project_name = fields.Str(required=True)
    contractor_name = fields.Str(required=True)
    nip = fields.Str(required=True)
    position = fields.Str(required=True)
    client_name = fields.Str(required=True)

    @validates('month')
    def validate_month(self, value):
        if value < 1 or value > 12:
            raise ValidationError(f'Invalid month ${value}. Month must be between 1 and 12')

    @validates('project_name')
    def validate_project(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid project name. Project name must be at least 1 character long')

    @validates('nip')
    def validate_nip(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid nip. NIP must be at least 1 character long')