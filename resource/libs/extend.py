from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword


@keyword(name='Drang And Drop')
def drag_drop(element_id, p_origin, p_target):
    """
    Implementação simplificada de drag and drop
    Para usar, você pode implementar usando coordenadas ou outros métodos
    """
    appiumLib = BuiltIn().get_library_instance('AppiumLibrary')
    driver = appiumLib._current_application()
    
    # Por enquanto, apenas log da operação
    # Implementação completa requer coordenadas específicas do dispositivo
    print(f"Drag and drop: {element_id} from {p_origin} to {p_target}")
    
    # Você pode implementar usando swipe com coordenadas:
    # driver.swipe(start_x, start_y, end_x, end_y, duration)
    
    return True
