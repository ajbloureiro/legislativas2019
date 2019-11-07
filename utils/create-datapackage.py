import datapackage

if __name__ == '__main__':
    package = datapackage.Package()
    package.infer('data/legislativeElectionResults.csv')

    package.descriptor['name'] = 'Resultados das eleições legislativas de vários anos'
    package.descriptor['title'] = 'Resultados das eleições legislativas de vários anos'
    package.descriptor['description'] = 'Resultados das eleições legislativas de vários anos'

    package.save('data/datapackage.json')
