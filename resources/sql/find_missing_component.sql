select module_detail.sort,
    module_detail.id_namespace as detail_ns,
    component.name as c_name
FROM module_detail
    LEFT JOIN component on module_detail.id_namespace = component.id_component
WHERE c_name is NULL ORDER By sort;