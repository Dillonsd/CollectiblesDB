from django.urls import path
from . import views

urlpatterns = [
    #List clients
    path('clients/', views.ClientList.as_view()),

    #List collectors/sellers
    path('clients/collectors/', views.CollectorList().as_view()),
    path('clients/sellers/', views.SellerList().as_view()),

    #Searching clients
    path('search/clients/<int:id>/<str:user>', views.ClientDetail.as_view()),
    path('search/clients/<int:id>', views.ClientDetail.as_view()),
    path('search/clients/<str:user>', views.ClientDetail.as_view()),
    path('search/clients/name/<str:clientname>', views.ClientDetail.as_view()),
    path('search/clients/phone/<int:num>', views.ClientDetail.as_view()),
    path('search/clients/collectors/<int:id>/<str:user>', views.CollectorDetail().as_view()),
    path('search/clients/sellers/<int:id>/<str:user>', views.SellerDetail().as_view()),
    path('search/clients/collectors/<int:id>', views.CollectorDetail().as_view()),
    path('search/clients/sellers/<int:id>', views.SellerDetail().as_view()),
    path('search/clients/collectors/<str:user>', views.CollectorDetail().as_view()),
    path('search/clients/sellers/<str:user>', views.SellerDetail().as_view()),
    path('search/clients/collectors/name/<str:clientname>', views.CollectorDetail().as_view()),
    path('search/clients/sellers/name/<str:clientname>', views.SellerDetail().as_view()),
    path('search/clients/collectors/phone/<int:num>', views.CollectorDetail().as_view()),
    path('search/clients/sellers/phone/<int:num>', views.SellerDetail().as_view()),

    #List albums
    path('collectibles/albums/', views.AlbumList.as_view()),

    #Searching albums
    path('search/collectibles/albums/<int:id>', views.AlbumDetail.as_view()),
    path('search/collectibles/albums/<str:albumName>', views.AlbumDetail.as_view()),
    path('search/collectibles/albums/type/<str:albumType>', views.AlbumDetail.as_view()),
    path('search/collectibles/albums/artist/<str:artistName>', views.AlbumDetail.as_view()),
    path('search/collectibles/albums/releaseyear/<int:release>', views.AlbumDetail.as_view()),

    #Album genres
    path('collectibles/albumGenre/', views.AlbumGenreList.as_view()),
    path('search/collectibles/albumGenre/<int:pk>',
         views.AlbumGenreDetails.as_view()),
     
    #List all comic books
    path('collectibles/comicBooks/', views.ComicBookList.as_view()),

    #Searching comic books
    path('search/collectibles/comicBooks/<int:id>', views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/<str:comicName>', views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/author/<str:authorName>', views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/illustrator/<str:illustratorName>', views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/releaseyear/<int:release>', views.ComicBookDetails.as_view()),

    #Comic genres
    path('collectibles/comicGenre/', views.ComicGenreList.as_view()),
    path('search/collectibles/comicGenre/<int:pk>',
         views.ComicGenreDetails.as_view()),

    #List all sport cards
    path('collectibles/sportCards/', views.SportCardList.as_view()),

    #Searching sport cards
    path('search/collectibles/sportCards/<int:id>', views.SportCardDetails.as_view()),
    path('collectibles/custom/', views.CustomList.as_view()),
    path('search/collectibles/custom/<int:pk>', views.CustomDetails.as_view()),
    path('collectibles/forms/', views.FormsList.as_view()),
    path('search/collectibles/forms/<int:pk>', views.formsDetails.as_view()),
    path('collectibles/madeOf/', views.MadeOfList.as_view()),
    path('search/collectibles/madeOf/<int:pk>', views.MadeOfDetails.as_view()),
    path('order/', views.OrderList.as_view()),
    path('search/order/<int:pk>', views.OrderListDetails.as_view()),
    path('order/fulfills/', views.FulfillsList.as_view()),
    path('search/order/fulfills/<int:pk>/<str:userName>/<int:orderID>',
         views.FulfillsDetails.as_view()),
    path('payment/', views.PaymentList.as_view()),
    path('search/payment/<int:pk>', views.PaymentDetails.as_view()),
    path('warehouse/', views.WarehouseList.as_view()),
    path('search/warehouse/<int:id>', views.WarehouseDetail.as_view()),
    path('search/warehouse/user/<int:id>', views.WarehouseListUser.as_view()),    #search warehouses by userid
    path('shipping_method/', views.ShippingMethodList.as_view()),
    path('search/shipping_method/<int:id>/<str:user>', views.ShippingMethodDetail.as_view()),
    path('moderates/', views.ModeratesList.as_view()),
    path('search/moderates/<int:id>/<str:user>', views.ModeratesDetail.as_view()),
    path('user_collection/', views.UserCollectionList.as_view()),
    path('search/user_collection/<int:id>/<str:user>', views.UserCollectionDetail.as_view()),
    path('consists_of/', views.ConsistsOfList.as_view()),
    path('search/consists_of/<int:id>/<int:userid>', views.ConsistsOfDetail.as_view()),
    path('sells/', views.SellsList.as_view()),
    path('search/sells/<int:id>/<int:userid>/<str:user>', views.SellsDetail.as_view()),
    path('wants/', views.WantsList.as_view()),
    path('search/wants/<int:id>/<str:user>', views.WantsDetail.as_view()),
    path('collection/', views.CollectionList.as_view()),
    path('search/collection/<int:id>', views.CollectionDetail.as_view()),
    path('manages/', views.ManagesList.as_view()),
    path('search/manages/<int:id>/<str:user>', views.ManagesDetail.as_view()),
    path('api/admin/', views.AdminList.as_view()),
    path('dealswith/', views.DealsWithList.as_view()),
    path('search/dealswith/<int:id>', views.DealsWithDetail.as_view()),
]