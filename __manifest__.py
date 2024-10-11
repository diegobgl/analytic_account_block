
{
    'name': 'Analytic Account Block',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Block Analytic Accounts from being selectable',
    'description': '''
        Adds functionality to block analytic accounts from being selectable in other models
        while still allowing access to reports and analytics.
    ''',
    'author': 'Custom Developer',
    'depends': ['account', 'analytic'],
    'data': [
        'views/account_analytic_account_view.xml',
    ],
    'installable': True,
    'application': False,
}
