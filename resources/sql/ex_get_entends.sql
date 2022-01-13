/*
Example of how to get extends for a given full namespace
*/
SELECT component.id_component, component.name, extends.namespace, extends.map_name, module_detail.sort FROM module_detail
LEFT JOIN component on module_detail.id_namespace = component.id_component
LEFT JOIN extends on component.id_component = extends.fk_component_id
WHERE module_detail.id_namespace = 'com.sun.star.accessibility.AccessibleContext'