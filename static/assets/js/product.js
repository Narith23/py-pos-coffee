function submitCreate() {
    let name = $("input[name=name]").val();
    let description = $("textarea[name=description]").val();
    let price = $("input[name=price]").val();
    let quantity = $("input[name=qty]").val();
    let category = $("select[name=category_id]").val();
    
    $.ajax({
        type: "POST",
        url: "/api/admin/products/web/create",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            name: name,
            description: description,
            price: price,
            qty: quantity,
            category_id: category
        }),
        success: function (response) {
            window.location.href = "/api/admin/products/web";
        }
    });
}