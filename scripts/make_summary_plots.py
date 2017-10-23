
# make a list of images in folder plots in markdown format
from tqdm import tqdm
from glob import glob
import datetime
import os
if __name__=='__main__':


    plots = sorted(glob('plots/*png'))
    template = "![{AltText}]({plot}  \"{Title}\")\n*{FigureCaption}*\n---\n"

    with open('plots_summary.md','w') as fout:
        print >> fout, '# Plots Summary\n'
        print >> fout, 'This is a self-generated list of the available plots'
        print >> fout, '**Dated:** *{:%d, %b %Y @ %H:%M}*'.format(datetime.datetime.now())
        print >> fout, '\n'
        for plot in tqdm(plots):
            os.system("convert {0:s} -trim -resize '1200x>' {0:s}".format(plot))
            print >> fout, template.format(AltText=plot,Title=plot,FigureCaption=plot,plot=plot)
