from deep_translator import GoogleTranslator
import config

def translate_text(text, target_language=config.TARGET_LANGUAGE):
    return GoogleTranslator(source='auto', target=target_language).translate(text)
