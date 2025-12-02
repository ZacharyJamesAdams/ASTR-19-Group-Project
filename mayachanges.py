# mpl.rcParams['font.family'] = ('arial' ,'serif', 'F')
f,ax = plt. subplots (1,1, figsize= (7,7))
for tick in ax. xaxis.get_ticklabels():
    tick.set_fontsize(20)
for tick in ax.yaxis.get_ticklabels():
    tick.set_fontsize(20)
def gaussian (x, mean, std):
    return (1/(std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
print (len (residuals) )
ax.hist(residuals,bins=10, range=(-0.75,0.75) ,alpha=0.5, edgecolor="white", density=True)
x_g = np.linspace(-5*res_std, 5*res_std, 1000)
ax.plot(x_g, gaussian(x_g, res_mean, res_std), color="red")
ax.set_xlim([-2,2])
ax.text(0.5,1.2,r' $\sigma = 0.25$', color='0', fontsize=32)
ax.set_xlabel('x',fontsize=20)
ax.set_ylabel('N(x)' ,fontsize=20)