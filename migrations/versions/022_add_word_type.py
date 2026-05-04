"""Add word_type column to words table for noun/verb/adjective classification

Revision ID: 022
Revises: 021
Create Date: 2026-04-24
"""
from alembic import op
import sqlalchemy as sa

revision = "022_add_word_type"
down_revision = "021_onboarding_v2_fields"
branch_labels = None
depends_on = None

# Top-frequency nouns from the HF word list to tag as 'noun'
_NOUN_IDS = [
    'tiempo', 'año', 'día', 'vez', 'hombre', 'señor', 'parte', 'lugar', 'vida', 'caso',
    'mundo', 'forma', 'país', 'manera', 'mujer', 'trabajo', 'punto', 'mano', 'tipo', 'cosa',
    'casa', 'grupo', 'gobierno', 'ciudad', 'agua', 'persona', 'palabra', 'gente', 'nombre',
    'problema', 'noche', 'proceso', 'momento', 'información', 'historia', 'ejemplo', 'nivel',
    'número', 'familia', 'estado', 'relación', 'dinero', 'pregunta', 'semana', 'empresa',
    'mes', 'vista', 'amor', 'acción', 'cambio', 'edad', 'tema', 'libro', 'carta', 'puerta',
    'niño', 'fin', 'campo', 'cara', 'padre', 'madre', 'centro', 'clase', 'nación', 'servicio',
    'razón', 'hijo', 'sistema', 'partido', 'ciudad', 'poder', 'presidente', 'ciudad', 'imagen',
    'tierra', 'paz', 'orden', 'lengua', 'sociedad', 'norte', 'papel', 'amigo', 'guerra',
    'programa', 'manera', 'camino', 'valor', 'fuerza', 'puesto', 'espacio', 'cabeza', 'cuerpo',
    'hora', 'tarde', 'mañana', 'noche', 'color', 'idea', 'plan', 'precio', 'empresa', 'vuelta',
    'banco', 'zona', 'mercado', 'sector', 'proyecto', 'avenida', 'calle', 'barrio', 'edificio',
    'oficina', 'tienda', 'restaurante', 'carro', 'perro', 'gato', 'mesa', 'silla', 'ventana',
    'comida', 'leche', 'carne', 'pan', 'café', 'vino', 'cerveza', 'jugo', 'té', 'arroz',
    'sol', 'luna', 'cielo', 'mar', 'río', 'montaña', 'parque', 'playa', 'bosque', 'lago',
    'ropa', 'camisa', 'zapato', 'falda', 'sombrero', 'bolsa', 'teléfono', 'computadora',
    'música', 'película', 'deporte', 'fútbol', 'viaje', 'hotel', 'aeropuerto', 'pasaporte',
]


def upgrade():
    op.add_column('words', sa.Column('word_type', sa.String(), nullable=True))
    op.create_index('ix_words_word_type', 'words', ['word_type'])

    noun_list = "', '".join(_NOUN_IDS)
    op.execute(f"""
        UPDATE words SET word_type = 'noun'
        WHERE id IN ('{noun_list}')
          AND word_type IS NULL
    """)


def downgrade():
    op.drop_index('ix_words_word_type', table_name='words')
    op.drop_column('words', 'word_type')
