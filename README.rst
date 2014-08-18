====================
Example of API proxy
====================

Install requirements and run app servers.

.. code-block:: console

    $ pip install -r requirements.txt
    $ honcho start

Install Nginx and copy config to ``/etc/nginx/conf.d/``.

.. code-block:: console

    $ sudo apt-get install nginx

Add ``127.0.0.1 internal.local external.local`` to ``/etc/hosts`` and
try to curl.

.. code-block:: console

    $ curl external.local
    Hi, I am internal API!
