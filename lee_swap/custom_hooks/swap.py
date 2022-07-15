from frappe.translate import update_translations_for_source
import frappe
import json

def on_update_swap(doc, method):
    translation_dict = {frappe.local.lang: doc.text_result}
    translation_data = json.dumps(translation_dict, indent=4)
    print(update_translations_for_source(doc.text_instance, translation_data))