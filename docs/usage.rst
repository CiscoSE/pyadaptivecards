=====
Usage
=====

A code sample says more then a thousand words so the following code snippet ...

.. code-block:: python 

    from pyadaptivecards.card import AdaptiveCard
    from pyadaptivecards.inputs import Text, Number
    from pyadaptivecards.components import TextBlock
    from pyadaptivecards.actions import Submit

    greeting = TextBlock("Hey hello there! I am a adaptive card")
    first_name = Text('first_name', placeholder="First Name")
    age = Number('age', placeholder="Age")

    submit = Submit(title="Send me!")

    card = AdaptiveCard(body=[greeting, first_name, age], actions=[submit])
    card_json = card.to_json(pretty=True)
    print(card_json)


... produces this json ...

.. code-block:: json

    {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "actions": [
            {
                "title": "Send me!",
                "type": "Action.Submit"
            }
        ],
        "body": [
            {
                "text": "Hey hello there! I am a adaptive card",
                "type": "TextBlock"
            },
            {
                "id": "first_name",
                "placeholder": "First name",
                "type": "Input.Text"
            },
            {
                "id": "age",
                "placeholder": "Age",
                "type": "Input.Number"
            }
        ],
        "type": "AdaptiveCard",
        "version": "1.1"
    }

which looks like this in Webex Teams.

.. image:: cards_sample.png

To explore all options and components have a look at the :ref:`api-documentation`.