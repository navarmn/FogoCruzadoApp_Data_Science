import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def plt_Rio_state(figsize=(10,8), alpha=1, cmap=None):
    rio_img = mpimg.imread('../figs/RJ_state.png')

    plt.figure(figsize=figsize)
    plt.imshow(rio_img, extent=[-44.93, -40.81, -23.43, -20.72], alpha=alpha)
    

def plt_Rio_city(figsize=None, alpha=1, cmap=None):
    rio_city_img = mpimg.imread('../figs/RJ_city.png')

    plt.figure(figsize=figsize)
    plt.imshow(rio_city_img, extent=(-43.906927, -42.987857, -23.081902, -22.736000), alpha=alpha)

def plt_density(X, s=20):

    sc = plt.scatter(X['LONGITUDE'], X['LATITUDE'], c=X['GUNFIRE'], 
                 s=X['GUNFIRE']*s, cmap=plt.get_cmap("Wistia"), alpha=0.5)

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    # cbar = plt.colorbar(sc)
    # cbar.set_label('Number of reports')