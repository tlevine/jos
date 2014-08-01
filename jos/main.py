import jos.download as d
import jos.parse as p

starting_url = 'http://www.degruyter.com/view/j/jos.2014.30.issue-2/issue-files/jos.2014.30.issue-2.xml'

def main():
    issues = set()
    links = {'issues': [starting_url], 'pdfs': []}

    while issues.union(links['issues']) != issues:
        response = None
        for issue in set(links['issues']).difference(issues):
            if response == None:
                response = d.get(issue)
            else:
                response = d.get(issue,
                    headers = {'referer': response.url},
                    cookies = dict(response.cookies))
            if not response.ok:
                raise ValueError('Bad issue response at %s' % response.url)
            issues.add(issue)

            links = p.links(response)
            for pdf in links['pdfs']:
                pdf_response = d.get(pdf,
                    headers = {'referer': response.url},
                    cookies = dict(response.cookies))
                if not pdf_response.ok:
                    raise ValueError('Bad PDF response at %s' % response.url)
