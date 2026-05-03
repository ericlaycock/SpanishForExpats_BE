"""Drop orphaned rows for the lessons consolidated in this round

Revision ID: 028_drop_merged_lessons
Revises: 027_drop_poss_adj_plural
Create Date: 2026-05-02

Lessons deleted in the consolidation pass:
  - grammar_irregular_present_ii_*_2 (hacer_poner, salir_decir, oir_caer, traer_valer)
  - grammar_spelling_changes_*_2 (conocer_producir, recoger_dirigir)
  - grammar_present_o_ue_*_2 (poder_volver, dormir_morir, mover_almorzar)
  - grammar_present_e_ie_*_2 (querer_pensar, cerrar_empezar, entender_preferir)
  - grammar_present_e_i_*_2 (pedir_servir, repetir_seguir)
  - grammar_present_e_i_vestir_elegir_1, _2 (entire group dropped)
  - grammar_irregular_present_ir_dar_2
  - grammar_irregular_present_tener_venir_2
  - grammar_irregular_present_ser_estar_2
  - grammar_ir_a_inf_vivir_escribir_2
  - grammar_ir_a_inf_dormir_estudiar_1, _2
  - grammar_modal_me_toca, grammar_modal_necesito (collapsed into tengo_que)
  - grammar_modal_chat_2 (collapsed into chat_1)
  - grammar_ser_estar_rules, grammar_ser_estar_rules_chat (folded into GL 4 ser+estar)

Removes their rows from every situations.id-FK table to avoid runtime
errors when a UserSituation/Conversation/etc. references a deleted sid.
"""
from alembic import op


revision = "028_drop_merged_lessons"
down_revision = "027_drop_poss_adj_plural"
branch_labels = None
depends_on = None


DEAD_SIDS = [
    # _2 deletions (workload merged into _1)
    "grammar_irregular_present_ii_hacer_poner_2",
    "grammar_irregular_present_ii_salir_decir_2",
    "grammar_irregular_present_ii_oir_caer_2",
    "grammar_irregular_present_ii_traer_valer_2",
    "grammar_spelling_changes_conocer_producir_2",
    "grammar_spelling_changes_recoger_dirigir_2",
    "grammar_present_o_ue_poder_volver_2",
    "grammar_present_o_ue_dormir_morir_2",
    "grammar_present_o_ue_mover_almorzar_2",
    "grammar_present_e_ie_querer_pensar_2",
    "grammar_present_e_ie_cerrar_empezar_2",
    "grammar_present_e_ie_entender_preferir_2",
    "grammar_present_e_i_pedir_servir_2",
    "grammar_present_e_i_repetir_seguir_2",
    "grammar_irregular_present_ir_dar_2",
    "grammar_irregular_present_tener_venir_2",
    "grammar_irregular_present_ser_estar_2",
    # Entire group drops
    "grammar_present_e_i_vestir_elegir_1",
    "grammar_present_e_i_vestir_elegir_2",
    # ir-a-inf trim
    "grammar_ir_a_inf_vivir_escribir_2",
    "grammar_ir_a_inf_dormir_estudiar_1",
    "grammar_ir_a_inf_dormir_estudiar_2",
    # Modal collapse
    "grammar_modal_me_toca",
    "grammar_modal_necesito",
    "grammar_modal_chat_2",
    # GL 4.1 ser_estar drops (folded into GL 4)
    "grammar_ser_estar_rules",
    "grammar_ser_estar_rules_chat",
    # construir/conseguir + convencer/continuar split into separate single-verb
    # lessons; the old combined _1/_2 sids are gone.
    "grammar_spelling_changes_construir_conseguir_1",
    "grammar_spelling_changes_construir_conseguir_2",
    "grammar_spelling_changes_convencer_continuar_1",
    "grammar_spelling_changes_convencer_continuar_2",
]


def upgrade() -> None:
    sids_csv = ", ".join(f"'{s}'" for s in DEAD_SIDS)
    # `user_milestone_events.conversation_id` FKs to conversations.id with no
    # ON DELETE clause, so deleting a referenced conversation row aborts the
    # transaction. Nullify the link first — see sibling migration 027 for
    # context.
    op.execute(
        f"UPDATE user_milestone_events SET conversation_id = NULL "
        f"WHERE conversation_id IN ("
        f"SELECT id FROM conversations WHERE situation_id IN ({sids_csv}))"
    )
    # NOT NULL situation_id → delete the row
    op.execute(f"DELETE FROM conversations WHERE situation_id IN ({sids_csv})")
    op.execute(f"DELETE FROM daily_encounter_logs WHERE situation_id IN ({sids_csv})")
    # PK includes situation_id → delete the row
    op.execute(f"DELETE FROM situation_words WHERE situation_id IN ({sids_csv})")
    op.execute(f"DELETE FROM user_situations WHERE situation_id IN ({sids_csv})")
    # Nullable FKs → null out, keep the parent
    op.execute(f"UPDATE user_words SET source_situation_id = NULL WHERE source_situation_id IN ({sids_csv})")
    op.execute(f"UPDATE user_milestone_events SET situation_id = NULL WHERE situation_id IN ({sids_csv})")
    op.execute(f"UPDATE sentence_hints SET situation_id = NULL WHERE situation_id IN ({sids_csv})")


def downgrade() -> None:
    pass
